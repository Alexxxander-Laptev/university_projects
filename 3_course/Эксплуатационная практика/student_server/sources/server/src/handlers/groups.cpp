/// Обработчик запроса на выдачу списка групп (реализация)
#include "groups.hpp"
#include <Poco/JSON/Parser.h>
#include <sstream>

using namespace Poco::Data::Keywords;
using namespace Poco::JSON;
extern Parser parser;

//Объявление статичных (static) членов класса
std::vector<Group> GroupsRequestHandler::cache;
bool GroupsRequestHandler::cacheOutdated = true;

//Реализация виртуальных методов родительских классов
Array GroupsRequestHandler::cacheArray() {
  Array arr; //Массив JSON для номеров групп
  for (Group g: cache)
    arr.add(g.name);
  return arr;
}

bool GroupsRequestHandler::cacheUpdate() {
  if (!cacheOutdated)
    return true;
  try {
    if (dbSession == nullptr)
	throw ConnectionFailedException("DB session is not specified");
    Statement query(*dbSession); //Объекта запроса базы данных
    Group g; //Промежуточные представление данных о группе
    /*Запись и выполнение запроса выборки (SELECT) с указанием полей
      для хранения данных и шага обхода запрашиваемой таблицы групп (groups)*/
    query << "SELECT * FROM groups ORDER BY name;", into(g.id), into(g.name), range(0, 1);
    while (!query.done()) {
      query.execute();
      cache.push_back(g);
    }
    //Уведомление об успешном обновлении кэша
    cacheOutdated = false;
    time_t cachedTime = time(nullptr);
    cout << "INFO: Successfully updated group list cache on " << ctime(&cachedTime);
  } catch (Poco::Exception ex) {
    //Предупреждение об ошибке обновления кэша (сервер хранит старые данные)
    cerr << ex.displayText() << endl;
    cout << "WARNING: Last cache update failed! The response data may be outdated." << endl;
    return false;
  }
  return true;
}

Object* GroupsRequestHandler::getResponseObject() {
  static Array actions;
  static Object required;
  if (actions.size() == 0) {
    for (auto action: {"add", "rename", "remove"}) {
      actions.add(action);
      Array props;
      props.add("name");
      if (action == "rename")
	props.add("newName");
      required.set(action, props);
    }
  }
  return responseObject(cacheArray(), actions, required, "");
}

/// Фабрика обработчиков HTTP-запросов (реализация)
#include "factory.hpp"
#include "groups.hpp"
#include "students.hpp"
#include "timerecords.hpp"
#include "agent.hpp"
#include "agents/timerecords.hpp"
#include "agents/groups.hpp"
#include "agents/students.hpp"
#include <sstream>
#include <vector>
#include <Poco/URI.h>

using namespace std;
using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Data;
typedef std::vector<string> svec;
typedef pair<string,string> QueryParameter;
typedef map<string, string> smap;
typedef std::vector<QueryParameter> QueryParameters;

template <class K, class V>
inline void extractIfExists(map<K, V> m, K key, V& to) {
  /*Извлечь значение key из таблицы m в переменную to, если оно там существует.
    Иначе, оставить переменной to её прежнее значение.*/
  try {
    to = m.at(key);
  } catch (std::out_of_range ex) {
    //Значение переменной to сохраняется
  }
}

template <class T>
bool valid(T v, std::vector<T> values) {
  // Проверить, соотвествует ли параметр одному из разрешённых значений
  auto it = find(values.begin(), values.end(), v);
  return it != values.end();
}

template <class Agent>
AgentRequestHandler* agentHandler(Session* dbSession) {
  //Двойной конструктор для обработчика и его агента
  return new AgentRequestHandler(new Agent(dbSession));
}

//Класс для вывода сообщений об ошибке
class ErrorRequestHandler: public HTTPRequestHandler {
  typedef HTTPResponse::HTTPStatus Status;
public:
  Status status;
  ErrorRequestHandler(Status status) {
    this->status = status;
  }
protected:
  void handleRequest(HTTPServerRequest& req, HTTPServerResponse& res) {
    res.setContentType("text/plain");
    res.setStatusAndReason(status);
    ostream& resBody = res.send();
    resBody << status << " - " << res.getReason() << endl;
    resBody.flush();
  }
};

//Конструктор класса
ReqFactory::ReqFactory(Session* dbSession){
  this->dbSession = dbSession;
}

//Метод-фабрикант (обработчик URI-адресов)
HTTPRequestHandler* ReqFactory::createRequestHandler(const HTTPServerRequest& req) {
  //Разбор адреса
  URI uri(req.getURI());
  string method = req.getMethod();
  bool isGET = (method == HTTPRequest::HTTP_GET);
  string path = uri.getPath(); //Относительный адрес ресурса
  cout << "INFO: Accepted " << method << " request for " << path << endl;
  cout.flush();
  vector<string> pathSeg; //Сегменты адреса (по '/')
  uri.getPathSegments(pathSeg);
  size_t pathSegN = pathSeg.size();
  const QueryParameters params = uri.getQueryParameters(); //GET-параметры в виде списка пар <ключ, значение>
  const smap paramMap(params.begin(), params.end()); //Таблица GET-параметров (для более удобной обработки)
  cout << "INFO: The request has " << pathSegN << " path segments and " << paramMap.size() << " parameters" << endl;
  
  //Обработка адреса
  if (pathSegN == 0)
    goto push_404;
  if (pathSeg[0] == "groups"){
    switch (pathSegN){
    case 2:{
      string groupName = path.substr(8); //Название запрашиваемой группы
      if (isGET) {
	string nameFormat; //Формат имён студентов в ответе сервера
	extractIfExists(paramMap, (const string)"nameFormat", nameFormat);
	if (!valid(nameFormat, {"split", "initials", "full"}))
	  nameFormat = StudentsRequestHandler::FORMAT_SPLIT; //Значение по умолчанию
	return new StudentsRequestHandler(dbSession, groupName, nameFormat);
      } else {
	if (StudentsRequestHandler::groupNames.size() == 0)
	  StudentsRequestHandler(dbSession).cacheUpdate(); //Обновляем кэш для получения информации о группах
	AgentRequestHandler* ah = agentHandler<StudentsAgent>(dbSession);
	if (pathSeg[1] != StudentsRequestHandler::GROUPS_ALL)
	  ah->getAgent()->defaults.set("group", pathSeg[1]);
	return ah;
      }
    }
    case 1:
      if (isGET)
	return new GroupsRequestHandler(dbSession);
      else
	return agentHandler<GroupsAgent>(dbSession);
    }
  } else if (pathSeg[0] == "timerecords") {
    if (isGET) {
      TimeRecordFilters filters; //Фильтры GET-запроса к журналу посещаемости
      //Заполнение фильтров из параметров запроса
      string* fields[] = {&filters.group, &filters.date, &filters.time, &filters.presence};
      static const string keys[] = {"group", "date", "time", "presence"};
      for (int i = 0; i < 4; i++)
      extractIfExists(paramMap, keys[i], *fields[i]);
    //Выполнение запроса
      return new TimeRecordsRequestHandler(dbSession, filters);
    } else {
      return agentHandler<TimeRecordAgent>(dbSession);
    }
  }
 push_404:
  cout << "WARNING: The request does not suit for any request handler. Returning 404..." << endl;
  return new ErrorRequestHandler(HTTPResponse::HTTP_NOT_FOUND);
}

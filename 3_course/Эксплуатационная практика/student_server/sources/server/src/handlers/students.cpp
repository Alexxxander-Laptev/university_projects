/// Обработчик запроса на список студентов (реализация)
#include "students.hpp"
#include "agents/students.hpp"
#include <sstream>
#include <codecvt>
#include <Poco/JSON/Array.h>
#include <Poco/JSON/Parser.h>
#include <Poco/Data/RecordSet.h>
#include <Poco/Dynamic/Var.h>

using namespace Poco::Data::Keywords;
using Poco::Dynamic::Var;
extern Parser parser;

//Методы структуры Student
string Student::fullName(bool initials) {
  static wstring_convert<codecvt_utf8_utf16<wchar_t>> converter; //Переводчик UTF-8 -> UTF-16
  ostringstream name; //Строковый поток полного имени
  name << lName << ' ';
  if (initials) {
    wstring initials[2]; //Для корректной обработки кириллицы используются "широкие" строки (wstring) 
    for (int i = 0; i < 2; i++){
      wstring wn = converter.from_bytes(i == 0 ? fName: mName);
      if (wn.substr(0, 2) == L"Дж")
	initials[i] = L"Дж"; //Исключение из правил составления инициалов
      else initials[i] += wn[0];
      name << converter.to_bytes(initials[i]) << '.';
    }
  } else {
    name << fName << ' ' << mName;
  }
  return name.str();
}

Object Student::JSONObject(string nameFormat) {
  Object obj;
  //Заполнение свойств объекта
  obj.set("id", id);
  obj.set("group", StudentsRequestHandler::groupNameById(groupId));
  if (nameFormat == StudentsRequestHandler::FORMAT_SPLIT) {
    obj.set("fName", fName);
    obj.set("lName", lName);
    obj.set("mName", mName);
  } else {
    bool init = (nameFormat == StudentsRequestHandler::FORMAT_INITIALS);
    obj.set("name", fullName(init));
  }
  return obj;
}

//Объявление статичных (static) членов класса
bool StudentsRequestHandler::cacheOutdated = true;
StudentCache StudentsRequestHandler::cache;
StudentCacheQueue StudentsRequestHandler::cacheOrder;
std::vector<string> StudentsRequestHandler::groupNames;
std::vector<int> StudentsRequestHandler::groupIds;

//Объявление конструктора
StudentsRequestHandler::StudentsRequestHandler(Session* dbSession, string group, string nameFormat): CachedRequestHandler(dbSession) {
  this->group = group;
  this->nameFormat = nameFormat;
};

//Собственные методы класса
inline bool StudentsRequestHandler::groupExists(string group) {
  if (group == GROUPS_ALL) //Проверка на техническую группу "all"
    return true;
  return find(groupNames.begin(), groupNames.end(), group) != groupNames.end();
}

int StudentsRequestHandler::groupIdByName(string name) {
  if (name == GROUPS_ALL)
    return GROUPS_ALL_ID;
  for (size_t i = 0; i < groupNames.size(); i++) {
    if (groupNames[i] == name)
      return groupIds[i];
  }
  return GROUPS_NULL; //Группа не найдена
}

const string StudentsRequestHandler::groupNameById(int id) {
  if (id == GROUPS_ALL_ID)
    return GROUPS_ALL;
  for (size_t i = 0; i < groupIds.size(); i++) {
    if (groupIds[i] == id)
      return groupNames[i];
  }
  return ""; //Группа не найдена
}

Array StudentsRequestHandler::cacheArray(string group){
  Array arr; //Массив JSON для объектов студентов
  Students studs; //Список студентов
  try {
    studs = cache[group];
  } catch (std::exception ex) {
    //Обновить кэш и повторно извлечь список студентов из него
    swap(this->group, group); //Временная замена
    cacheUpdate();
    swap(this->group, group);
    studs = cache[group];
  }
  for (Student stud: studs) {
    //cout << "Adding student ID " << stud.id << " from " << group << endl;
    arr.add(stud.JSONObject(nameFormat));
  }
  return arr;
}

Students StudentsRequestHandler::getStudentsFromDB(int groupId) {
  if (dbSession == nullptr)
    throw ConnectionFailedException("DB session is not specified");
  Statement statement(*dbSession);
  //Текст запроса
  string query = "SELECT * FROM students";
  if (groupId == GROUPS_ALL_ID)
    query += ";";
  else
    query += " WHERE groupId = " + to_string(groupId) + ";";
  cout << groupId << endl;
  Students studs; //Список студентов
  statement << query, now;
  RecordSet rs(statement);
  for (Row row: rs) {
    Student stud = {row.get(0), row.get(1), //id, fName
		    row.get(2), row.get(3), row.get(4)}; //lName, mName, groupId
    studs.push_back(stud);
  }
  return studs;
}

Students StudentsRequestHandler::getStudentsFromDB(string group) {
  return getStudentsFromDB(groupIdByName(group));
}

//Реализация виртутальных методов родительских классов
Array StudentsRequestHandler::cacheArray() {
  Array arr; //Массив итоговых данных
  for (string group: cacheOrder) {
    //Парсируем информацию по конкретным группам
    Array studs = cacheArray(group);
    Object gobj;
    gobj.set("group", group);
    gobj.set("students", studs);
    arr.add(gobj);
  }
  return arr;
}

bool StudentsRequestHandler::cacheUpdate() {
  try {
    if (dbSession == nullptr)
	throw ConnectionFailedException("DB session is not specified");
    if (cacheOutdated || groupNames.size() == 0) {
      //Очистка кэша от устаревших данных
      groupNames.clear();
      groupIds.clear();
      cacheOrder.clear();
      cache.clear();
      //Получаем список всех групп
      Statement query(*dbSession);
      query << "SELECT * FROM groups;", into(groupIds), into(groupNames), now;
      time_t cachedTime = time(nullptr);
      cout << "INFO: Successfully updated group list on " << ctime(&cachedTime);
      cacheOutdated = false;
    }
    auto order = find(cacheOrder.begin(), cacheOrder.end(), group);
    if (order != cacheOrder.end()) {
      //Группа уже есть в кэше, обновить её положение в очереди
      cacheOrder.erase(order);
      cacheOrder.push_back(group);
    }
    else if (groupExists(group)) {
      //Если группа вообще существует в списке
      if (cacheOrder.size() >= CACHE_SIZE) {
	//Очистка кэша от данных, к которым давно не обращались
	cache.erase(cacheOrder.front());
	cacheOrder.pop_front();
      }
      //Добавление списка группы в кэш
      Students dbData = getStudentsFromDB(group);
      cache[group] = dbData;
      if (cacheOrder.size() == CACHE_SIZE - 1)
	cout << "WARNING: The student data cache is going to be overflowed. Old data will be erased until they are required again." << endl;
      cacheOrder.push_back(group);
      time_t cachedTime = time(nullptr);
      cout << "INFO: Cached student data for group " << group << " on " << ctime(&cachedTime);
    }
  } catch (Poco::Exception ex) {
    cerr << "Student cache update error!" << endl;
    cerr << ex.displayText() << endl;
    return false;
  }
  return true;
}

Object* StudentsRequestHandler::getResponseObject() {
  cout << "Formating the response..." << endl;
  static Array actions;
  static Object required;
  if (actions.size() == 0) {
    StudentsAgent sa(dbSession); //Для доступа к вирутальным методам
    for (auto action: sa.PURPOSE_ALL) {
      actions.add(action);
      Array props;
      for (auto prop: sa.requiredProperties(action))
	props.add(prop);
      required.set(action, props);
    }
  }
  try {
    Object* obj = responseObject(cacheArray(group), actions, required, "?group=" + group);
    cout << "Checking response...";
    //Извлекаем массив ч/з парсинг его JSON-представления (из-за неопознанной ошибки при извлечении массива напрямую)
    Var data = obj->get("data");
    data = parser.parse(data.toString());
    obj->set("data", data);
    //Возврат объекта
    return obj;
  } catch (std::exception ex) {
    cerr << ex.what() << endl;
  }
  return new Object();
}

void StudentsRequestHandler::handleRequest(HTTPServerRequest& req, HTTPServerResponse& res) {
  cacheUpdate(); //Обновляем кэш из базы данных
  //Проверка на существование группы
  if (!groupExists(group)) {
    //Группа не найдена, отправка пустого сообщения с кодом 404
    cout << "WARNING: Attempt to require data for a missing group " << group << ". ";
    cout << "Returning 404..." << endl;
    respondError(res, HTTPResponse::HTTP_NOT_FOUND);
  } else {
    //Отправка ответа в формате JSON
    CachedRequestHandler::handleRequest(req, res);
  }
}

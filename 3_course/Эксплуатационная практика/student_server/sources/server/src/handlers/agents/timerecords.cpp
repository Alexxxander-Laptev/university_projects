/// Агент взаимодействия с таблицей посещаемости (реализация)
#include "timerecords.hpp"
#include "../timerecords.hpp"
#include <Poco/Net/NetException.h>
#include <Poco/Dynamic/Var.h>

using namespace Poco::Data::Keywords;
using Poco::Dynamic::Var;
typedef std::vector<int> ivec;

//Вспомогательные функции
inline void TimeRecordAgent::outdateCache() {
  TimeRecordsRequestHandler::cacheOutdated = true;
}

const std::vector<string> TimeRecordAgent::requiredProperties() {
  return {"id", "date", "time"};
}

//Добавление
bool TimeRecordAgent::add(int id, string date, string time, bool present) {
  try {
    prepare();
    *sql << "INSERT INTO timerecords VALUES ($1, $2, $3, $4);", use(id),
      use(date), use(time), use(present), now;
    outdateCache();
    return true;
  } catch(ExecutionException ex) {
    //Ничего не делает, т.к. отчёты об ошибках в запросах обычно выводит СУБД
  }
  return false;
}

bool TimeRecordAgent::add(const Object& obj) {
  Object cObj = obj; //Дополненная версия объекта
  bool completed = complete(cObj); //Дополняем объект при необходимости
  if (!completed)
    throw MessageException("Insufficent data to complete the request", 1);
  if (obj.has("present")) { //В объекте указаны изменения посещаемости
    int id = obj.getValue<int>("id");
    string d = obj.getValue<string>("date");
    string t = obj.getValue<string>("time");
    bool p = obj.getValue<bool>("present");
    return add(id, d, t, p);
  }
  return false; //Нет данных об оценке
}

//Изменение
bool TimeRecordAgent::alter(int id, string date, string time, bool present) {
  try {
    prepare();
    *sql << "UPDATE timerecords SET presence = $1 WHERE studId = $2 AND date = $3 AND time = $4;", use(present), use(id), use(date), use(time);
    size_t altered = sql->execute();
    if (altered == 0) { //Изменений не было => нет записи в БД
      if (addIfNotExist)
	return add(id, date, time, present); //Создать запись в БД
      return false; //Невозможно изменить несуществующую запись
    }
    outdateCache();
    return true;
  } catch(ExecutionException ex) {
    //Ничего не делает, т.к. отчёты об ошибках в запросах обычно выводит СУБД
  }
  return false;
}

bool TimeRecordAgent::alter(const Object& obj) {
  Object cObj = obj; //Дополненная версия объекта
  bool completed = complete(cObj); //Дополняем объект при необходимости
  if (!completed)
    throw MessageException("Insufficent data to complete the request", 1);
  if (obj.has("present")) { //В объекте указаны изменения посещаемости
    int id = obj.getValue<int>("id");
    string d = obj.getValue<string>("date");
    string t = obj.getValue<string>("time");
    bool p = obj.getValue<bool>("present");
    return alter(id, d, t, p);
  }
  return true; //Нет данных об изменениях => нечего изменять
}

//Удаление
bool TimeRecordAgent::remove(int id, string date, string time) {
  try {
    prepare();
    *sql << "DELETE FROM timerecords WHERE studId = $1 AND date = $2 AND time = $3;", use(id), use(date), use(time);
    size_t altered = sql->execute();
    if (altered == 0) //Изменений не было => нет записи в БД
      return ignoreIdleRemoval;
    outdateCache();
    return true;
  } catch(ExecutionException ex) {
    //Ничего не делает, т.к. отчёты об ошибках в запросах обычно выводит СУБД
  }
  return false;
}

bool TimeRecordAgent::remove(const Object& obj) {
  Object cObj = obj; //Дополненная версия объекта
  bool completed = complete(cObj); //Дополняем объект при необходимости
  if (!completed)
    throw MessageException("Insufficent data to complete the request", 1);
  int id = obj.getValue<int>("id");
  string d = obj.getValue<string>("date");
  string t = obj.getValue<string>("time");
  return remove(id, d, t);
}

///Базовый класс для агентов взаимодействия с базой данных (реализация)
#include "agent.hpp"
#include <Poco/Dynamic/Var.h>

using Poco::Dynamic::Var;

DBAgent::DBAgent(Session* dbSession, const Object& defaults) {
  this->dbSession = dbSession;
  this->sql = new Statement(*dbSession);
  this->defaults = defaults;
}

DBAgent::~DBAgent() {
  if (sql != nullptr)
    delete sql;
}

bool DBAgent::complete(Object& obj) {
  for (string prop: requiredProperties()) {
    Var defaultValue = defaults.get(prop); //isEmpty() = true, если ключ prop не задан
    if (!obj.has(prop) && !defaultValue.isEmpty())
      obj.set(prop, defaultValue);
  }
  return full(obj);
}

bool DBAgent::full(const Object& obj) {
  for (string prop: requiredProperties())
    if (!obj.has(prop))
      return false; //Объект имеет неполный набор свойств
  return true; //Объект имеет все необходимые свойства
}

bool DBAgent::act(const string& method, const Object& obj) {
  if (method == "add")
    return add(obj);
  if (method == "remove")
    return remove(obj);
  return alter(obj); //Метод по умолчанию
}

const std::vector<string> DBAgent::requiredProperties() {
  return {}; //По умолчанию у агента нет требований к свойствам JSON-объектов
}

Session* DBAgent::getDBSession() {
  return dbSession;
}

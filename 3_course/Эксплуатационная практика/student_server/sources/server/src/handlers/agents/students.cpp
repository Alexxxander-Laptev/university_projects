///Класс агента взаимодействия с таблицей студентов (реализация)
#include "students.hpp"
#include "../students.hpp"
#include "groups.hpp" //Для добавление/удаление групп используется GroupsAgent
#include <Poco/Dynamic/Var.h>

using namespace Poco::Data::Keywords;
using Poco::Dynamic::Var;

const char* StudentsAgent::PURPOSE_ALL[] = {"add", "move", "rename", "alter", "remove"};

const std::vector<string> StudentsAgent::requiredProperties() {
  return {"id", "group", "fName", "lName"};
}

const std::vector<string> StudentsAgent::requiredProperties(const string& purpose) {
  if (purpose == PURPOSE_ADD)
    return {"fName", "lName"};
  if (purpose == PURPOSE_RENAME)
    return {"id", "fName", "lName", "mName"};
  if (purpose == PURPOSE_MOVE)
    return {"id", "group"};
  if (purpose == PURPOSE_ALTER)
    return{"id", "fName", "lName", "mName", "group"};
  if (purpose == PURPOSE_REMOVE)
    return {"id"};
  return requiredProperties(); //Вернуть общий список
}

void StudentsAgent::outdateCache() {
  StudentsRequestHandler::cacheOutdated = true;
}

inline void StudentsAgent::manualComplete(Object& obj) {
  //Дополнения без использования циклов
  //Заполнение очества пустой строкой при его отсутствии
  if (!obj.has("mName"))
    obj.set("mName", "");
  //Заполнение поля группы из адреса или переданного в теле значения по умолчнию
  Var group = defaults.get("group");
  if (!obj.has("group") && !group.isEmpty())
    obj.set("group", group);
}

bool StudentsAgent::complete(Object& obj) {
  manualComplete(obj);
  return DBAgent::complete(obj); //Стандартная процедура дополнения
}

bool StudentsAgent::complete(Object& obj, const string& purpose) {
  for (string prop: requiredProperties(purpose)) {
    Var defaultValue = defaults.get(prop);
    if (!obj.has(prop) && !defaultValue.isEmpty())
      obj.set(prop, defaultValue);
  }
  manualComplete(obj);
  return full(obj, purpose);
}

bool StudentsAgent::full(const Object& obj, const string& purpose) {
  for (string prop: requiredProperties(purpose))
    if (!obj.has(prop))
      return false; //Объект имеет неполный набор свойств
  return true; //Объект имеет все необходимые свойства
}

int StudentsAgent::groupIdByName(string name) {
  //ИД и названия групп из StudentsRequestHandler
  static std::vector<int>& groupIds = StudentsRequestHandler::groupIds;
  static std::vector<string>& groupNames = StudentsRequestHandler::groupNames;
  for (size_t i =0; i < groupNames.size(); i++) {
    if (groupNames[i] == name)
      return groupIds[i];
  }
  return NULL_GROUP; //Группа не найдена
}

int StudentsAgent::resolveGroupName(string group) {
  int groupId = groupIdByName(group);
  if (groupId == NULL_GROUP && addGroupIfNotExists) {
    //Добавляем новую группу
    GroupsAgent ga(dbSession);
    ga.add(group, &groupId); //Если группа не добавится, значение groupId останется прежним
  }
  if (groupId == NULL_GROUP)
    throw MessageException("Specified group does not exist", 1);
  return groupId;
}

bool StudentsAgent::add(int groupId, string fName, string lName, string mName) {
  prepare();
  cout << "Adding student " << fName << ' ' << mName << ' ' << lName << " to group #" << groupId << "..." << endl;
  *sql << "INSERT INTO students (fName, lName, mName, groupId) VALUES ($1, $2, $3, $4);", use(fName), use(lName), use(mName), use(groupId);
  outdateCache();
  return sql->execute() != 0;
}

bool StudentsAgent::add(string group, string fName, string lName, string mName)
{
  return add(resolveGroupName(group), fName, lName, mName);
}

bool StudentsAgent::add(const Object& obj) {
  Object cobj = obj; //Полный объект
  bool completed = complete(cobj, PURPOSE_ADD);
  if (completed) {
    static const string keys[] = {"group", "fName", "lName", "mName"};
    string data[4];
    for (int i = 0; i < 4; i++)
      data[i] = cobj.getValue<string>(keys[i]);
    return add(data[0], data[1], data[2], data[3]);
  }
  throw MessageException("Insufficent data to complete the request", 1);
}

bool StudentsAgent::rename(int id, string fName, string lName, string mName) {
  prepare();
  cout << "Renaming student #" << id << " to " << fName << ' ' << mName << ' ' << lName << "..." << endl;
  *sql << "UPDATE students SET fName = $1, lName = $2, mName = $3 WHERE id = $4;", use(fName), use(lName), use(mName), use(id);
  outdateCache();
  return sql->execute() != 0;
}

bool StudentsAgent::move(int id, int groupId) {
  prepare();
  cout << "Transfering student #" << id << " to group #" << groupId << "..." << endl;
  *sql << "UPDATE students SET groupId = $1 WHERE id = $2;", use(groupId), use(id);
  outdateCache();
  return sql->execute() != 0;
}

bool StudentsAgent::move(int id, string group) {
  return move(id, resolveGroupName(group));
}

bool StudentsAgent::alter(const Object& obj) {
  Object cobj = obj; //Полный объект
  complete(cobj);
  if (cobj.has("id")) {
    int id = cobj.getValue<int>("id");
    bool success = true; //Все операции прошли успешно
    bool full_rn = full(cobj, PURPOSE_RENAME);
    bool full_mv = full(cobj, PURPOSE_MOVE);
    if (full_rn) {
      static auto keys = requiredProperties(PURPOSE_RENAME);
      string name[3];
      for (int i = 1; i < 4; i++) { //Ключ keys[0]="id" пропускается
	name[i-1] = cobj.getValue<string>(keys[i]);
      }
      success = rename(id, name[0], name[1], name[2]) && success;
    }
    if (full_mv) {
      string group = cobj.getValue<string>("group");
      success = move(id, group) && success;
    } else if (!full_rn) {
      //Ни одна из операций не может быть выполнена
      goto alter_exception;
    }
    return success;
  }
 alter_exception:
  throw MessageException("Insufficent data to complete the request", 1);
}

bool StudentsAgent::remove(int id) {
  prepare();
  cout << "Removing student #" << id << " from the database..." << endl;
  int groupId; //Группа удалённого студента
  *sql << "DELETE FROM students WHERE id = $1 RETURNING (students.groupId);", use(id), into(groupId);
  int qnt = sql->execute(); //Количество удалённых элементов (1 или 0)
  if (qnt != 0 && removeGroupIfEmpty) {
    int left; //Количество оставшихся студентов в группе
    left = StudentsRequestHandler::getStudentsFromDB(groupId).size();
    if (left <= 0) {
      GroupsAgent ga(dbSession);
      ga.remove(groupId);
    }
  }
  outdateCache();
  return qnt != 0;
}

bool StudentsAgent::remove(const Object& obj) {
  if (!obj.has("id"))
    throw MessageException("Insufficent data to complete the request", 1);
  return remove(obj.getValue<int>("id"));
}


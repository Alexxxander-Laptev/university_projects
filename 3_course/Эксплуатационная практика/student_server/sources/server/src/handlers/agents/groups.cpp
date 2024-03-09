///Класс агента взаимодействия с таблицей посещаемости (реализация)
#include "groups.hpp"
#include "../groups.hpp"
#include <Poco/Data/Statement.h>
#include <Poco/Data/RecordSet.h>

using namespace Poco::Data::Keywords;

void GroupsAgent::outdateCache() {
  GroupsRequestHandler::cacheOutdated = true;
}

bool GroupsAgent::add(string name, int* idStorage) {
  prepare();
  cout << "Adding group " << name << " to the database..." << endl;
  *sql << "INSERT INTO groups (name) VALUES ($1);", use(name);
  size_t qnt = sql->execute(); //Кол-во добавленных строк (1 или 0)
  if (idStorage != nullptr && qnt != 0) {
    RecordSet rs(*sql);
    int id = rs.row(0).get(0).convert<int>();
    *idStorage = id;
    cout << "INFO: The new group ID (" << id << ") was written to pointer " << idStorage << endl;
  }
  if (qnt != 0)
    outdateCache();
  return qnt != 0;
}

bool GroupsAgent::add(const Object& obj) {
  if (obj.has("name"))
    return add(obj.getValue<string>("name"));
  throw MessageException("Insufficent data to complete the request", 1);
}

bool GroupsAgent::alter(int id, string newName) {
  prepare();
  cout << "Renaming group #" << id << " to " << newName << endl;
  *sql << "UPDATE groups SET name = $1 WHERE id = $2;", use(newName), use(id);
  outdateCache();
  return sql->execute() != 0;
}

bool GroupsAgent::alter(string name, string newName) {
  prepare();
  cout << "Renaming group " << name << " to " << newName << endl;
  *sql << "UPDATE groups SET name = $1 WHERE name = $2;", use(newName), use(name);
  outdateCache();
  return sql->execute() != 0;
}

bool GroupsAgent::alter(const Object& obj) {
  if (obj.has("newName")) {
    string newName = obj.getValue<string>("newName");
    if (obj.has("name"))
      return alter(obj.getValue<string>("name"), newName);
    if (obj.has("id"))
      return alter(obj.getValue<int>("id"), newName);
  }
  throw MessageException("Insufficent data to complete the request", 1);
}

bool GroupsAgent::remove(int id) {
  prepare();
  cout << "Removing group #" << id << " from the database..." << endl;
  *sql << "DELETE FROM groups WHERE id = $1;", use(id);
  outdateCache();
  return sql->execute() != 0;
}

bool GroupsAgent::remove(string name) {
  prepare();
  cout << "Removing group " << name << " from the database..." << endl;
  *sql << "DELETE FROM groups WHERE name = $1;", use(name);
  return sql->execute() != 0;
}

bool GroupsAgent::remove(const Object& obj) {
  if (obj.has("name"))
    return remove(obj.getValue<string>("name"));
  if (obj.has("id"))
    return remove(obj.getValue<int>("id"));
  throw MessageException("Insufficent data to complete the request", 1);
}

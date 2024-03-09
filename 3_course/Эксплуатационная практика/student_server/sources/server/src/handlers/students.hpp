/// Обработчик запроса на список студентов (заголовок)
#include "cached.hpp"
#include <vector>
#include <map>
#include <list>
#include <Poco/JSON/Object.h>
#ifndef HANDLERS_STUDENTS_HPP_INCLUDED
#define HANDLERS_STUDENTS_HPP_INCLUDED

using namespace Poco::JSON;

struct Student { //Информация о студенте
  int id; //ИД студента в базе данных (БД)
  string fName, lName, mName; //ФИО студента (раздельно)
  string fullName(bool initials); //ФИО студента (слитно)
  size_t groupId; //ИД группы студента
  Object JSONObject(string nameFormat); //Перевод в формат JSON
};

typedef std::vector<Student> Students;
typedef map<string, Students> StudentCache;
typedef list<string> StudentCacheQueue;

class StudentsRequestHandler: public CachedRequestHandler {
  typedef const char* strconst; //Тип для строковых констант
  friend Student; //Предоставить структуре Student доступ ко всем членам класса
  friend class StudentsAgent; //Предоставить агенту доступ ко всем членам класса
  friend class ReqFactory;
public:
  StudentsRequestHandler(Session* dbSession, string group = GROUPS_ALL, string nameFormat = FORMAT_SPLIT);
  static bool cacheOutdated; //Данные в кэше устарели или отсутствуют
  static bool groupExists(string); //Проверка на существование группы (из кэша групп)
  bool cacheUpdate() override; //Обновить кэш списка вручную (true, если успешно)
  Array cacheArray() override; //Данные кэша в формате JSON
  Array cacheArray(string group); //Данные по конкретной группе в формате JSON
  static Students getStudentsFromDB(string group = GROUPS_ALL); //Вернуть список студентов из БД
  static Students getStudentsFromDB(int groupId);
  Object* getResponseObject() override; //Ответ на запрос списка групп
  // Параметры обработки запроса
  string group, nameFormat;
  // Форматы имён и прочие константы
  static constexpr strconst GROUPS_ALL = "all"; //Ключ для вывода студентов из всех групп
  static constexpr int GROUPS_NULL = -1; //ID для отсутствующей группы
  static constexpr int GROUPS_ALL_ID = -2; //ID для ключа GROUPS_ALL
  static constexpr strconst FORMAT_SPLIT = "split"; //Выводить значения ФИО раздельно (fName, lName, mName)
  static constexpr strconst FORMAT_FULL = "full"; //Выводить ФИО одной строкой (name) полностью
  static constexpr strconst FORMAT_INITIALS = "initials"; //Выводить ФИО одной строкой (name) с инициалами
private:
  static StudentCache cache; //Кэш списка студентов в каждой группе (ключ "all" хранит всех студентов в БД)
  static StudentCacheQueue cacheOrder; //Очередь с порядком добавления элементов в кэш
  static const int CACHE_SIZE = 10; //Максимальное количество записей, которое может храниться в кэше
  static vector<string> groupNames; //Названия всех групп (не только из кэша)
  static vector<int> groupIds; //ИД всех групп (параллельно их названиям в groupNames)
  static int groupIdByName(string name); //ИД группы по её названию
  static const string groupNameById(int id); //Название группы по её ИД
  void handleRequest(HTTPServerRequest& req, HTTPServerResponse& res) override;
};
#endif

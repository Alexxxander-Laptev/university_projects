///Класс агента взаимодействия с таблицей студентов (заголовок)
#include "agent.hpp"
#include "../students.hpp"
#ifndef HANDLERS_AGENT_STUDENTS_HPP_INCLUDED
#define HANDLERS_AGENT_STUDENTS_HPP_INCLUDED

using namespace std;
using namespace Poco::Data;

class StudentsAgent: public DBAgent {
protected:
  inline void outdateCache(); //Объявить кэш GET-запросов устаревшим
public:
  //Конструктор класса
  using DBAgent::DBAgent;
  //Парамтеры работы с таблицей групп при выполнении запросов
  bool addGroupIfNotExists = false; //Создавать новую группу для студента, если она не существует в БД
  bool removeGroupIfEmpty = false; //Удалять группу, если в ней не осталось студентов
  //Дополнение объектов
  bool complete(Object& obj) override; //Дополнение без предназначения
  bool complete(Object& obj, const string& purpose); //Дополнение для конкретной операции
  bool full(const Object& obj, const string& purpose); //Проверка на полноту данных для конкретной операции
  //Добавление нового студента (true при успехе)
  bool add(int groupId, string fName, string lName, string mName = "");
  bool add(string group, string fName, string lName, string mName = ""); //ИД группы по её имени
  bool add(const Object& obj) override;
  //Изменение данных студента (true при успехе)
  bool rename(int id, string fName, string lName, string mName = ""); //Переименовать студента
  bool move(int id, int groupId); //Переместить студента в другую группу
  bool move(int id, string group); //ИД группы по её имени
  bool alter(const Object& obj) override; //rename() + move()
  //Удаление студента из БД (true при успехе)
  bool remove(int id);
  bool remove(const Object& obj) override;
  //Константы
  static constexpr int NULL_GROUP = -1;
  static constexpr const char* PURPOSE_ADD = "add"; //Добавление студента
  static constexpr const char* PURPOSE_RENAME = "rename"; //Переименование студента
  static constexpr const char* PURPOSE_MOVE = "move"; //Перевод студента в другую группу
  static constexpr const char* PURPOSE_ALTER = "alter"; //Полное изменение данных о студенте
  static constexpr const char* PURPOSE_REMOVE = "remove"; //Удаление студента
  static const char* PURPOSE_ALL[5]; //Список всех действий
  //Списки обязательных свойств JSON-объектов
  const std::vector<string> requiredProperties() override; //Общий список обязательных свойств
  const std::vector<string> requiredProperties(const string& purpose); //Список обязательных свойств для конкретной операции
protected:
  //Поиск группы по её имени
  static int groupIdByName(string name); //ИД группы по её имени. При неудаче возращеает NULL_GROUP;
  int resolveGroupName(string name); //Получить ИД существующей группы по её имени или создать новую с этим именем (если это разрешено). При неудаче поднимет исключение MessageException.
  inline void manualComplete(Object& obj); //Уникальные для этого класса дополнения без циклов
};
#endif

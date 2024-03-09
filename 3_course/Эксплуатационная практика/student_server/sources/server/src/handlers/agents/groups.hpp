///Класс агента взаимодействия с таблицей посещаемости (заголовок)
#include "agent.hpp"
#ifndef HANDLERS_AGENT_GROUPS_HPP_INCLUDED
#define HANDLERS_AGENT_GROUPS_HPP_INCLUDED

using namespace std;
using namespace Poco::Data;

class GroupsAgent: public DBAgent {
  friend class AlterGroupsRequestHandler;
protected:
  inline void outdateCache(); //Объявить кэш GET-запросов устаревшим
public:
  //Конструктор класса
  using DBAgent::DBAgent; 
  //Добавление новой группы в БД (true при успехе)
  bool add(string name, int* idStorage = nullptr); //ID добавленной группы записывается по указателю idStorage
  bool add(const Object& obj) override;
  //Изменение названия группы в БД (true при успехе)
  bool alter(int id, string newName); //По ИД группы в БД
  bool alter(string name, string newName); //По старому названию
  bool alter(const Object& obj) override;
  //Удаление группы из БД (true при успехе, вместе с группой удаляются все студенты в ней)
  bool remove(int id); //По ИД группы в БД
  bool remove(string name); //По названию группы
  bool remove(const Object& obj) override;
};
#endif

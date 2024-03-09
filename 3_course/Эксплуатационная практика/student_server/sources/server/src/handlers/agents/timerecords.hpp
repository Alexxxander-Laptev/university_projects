///Класс агента взаимодействия с таблицей посещаемости
#include "agent.hpp"
#include "../agent.hpp"
#ifndef HANDLERS_AGENT_TIMERECORDS_HPP_INCLUDED
#define HANDLERS_AGENT_TIMERECORDS_HPP_INCLUDED

class TimeRecordAgent: public DBAgent {
protected:
  inline void outdateCache(); //Объявить кэш GET-запросов устаревшим
public:
  //Конструктор класса
  using DBAgent::DBAgent;
  //Добавление строк в БД (true при успехе)
  bool add(int id, string date, string time, bool present); //Полный вызов
  bool add(const Object& obj) override; //Вывоз с JSON-объектом
  //Изменение строк в БД (true при успехе)
  bool alter(int id, string date, string time, bool present); //Полный вызов
  bool alter(const Object& obj) override; //Вывоз с JSON-объектом
  //Удаление записей из БД (true при успехе)
  bool remove(int id, string date, string time); //Полный вызов
  bool remove(const Object& obj) override; //Вывоз с JSON-объектом
  //Проверка JSON-объектов
  const std::vector<string> requiredProperties() override; //Необх. свойства поступающих объектов
};
#endif

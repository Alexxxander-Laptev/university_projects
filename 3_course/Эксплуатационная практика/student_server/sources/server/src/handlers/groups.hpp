/// Обработчик запроса на выдачу списка групп (заголовок)
#include "cached.hpp"
#include <vector>
#ifndef HANDLERS_GROUPS_HPP_INCLUDED
#define HANDLERS_GROUPS_HPP_INCLUDED

struct Group {
  int id; //ИД группы в базе данных (БД)
  string name; //Название (номер) группы
};

class GroupsRequestHandler: public CachedRequestHandler {
public:
  static bool cacheOutdated; //Данные в кэша устарели или отсутствуют
  using CachedRequestHandler::CachedRequestHandler; // Использовать родительский конструктор
  bool cacheUpdate() override; //Обновить кэш списка вручную (true, если успешно)
  Array cacheArray() override; //Список групп из кэша в формате JSON
  Object* getResponseObject() override; //Ответ на запрос списка групп
private:
  static std::vector<Group> cache; //Кэш списка групп
};
#endif


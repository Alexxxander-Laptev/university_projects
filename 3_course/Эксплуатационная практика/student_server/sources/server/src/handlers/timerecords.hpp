/// Обработчик запроса на записи о посещаемости (заголовок)
#include "cached.hpp"
#include <vector>
#include <map>
#include <list>
#include <Poco/JSON/Object.h>
#ifndef HANDLERS_TIMERECORDS_HPP_INCLUDED
#define HANDLERS_TIMERECORDS_HPP_INCLUDED

using namespace Poco::JSON;
using Poco::DateTime;

struct TimeRecord { //Информация о посещаемости студента
  int id; //ИД студента в базе данных (БД)
  string date; //Дата занятия
  string time; //Время занятия
  bool present = false; //Отметка о присутствии студента в указанное время
  Object JSONObject(); //Перевод в JSON
};

struct TimeRecordFilters {
  //Параметры фильтрации результатов GET-запроса
  string group = GROUP_ANY;
  string date = DATE_ANY;
  string time = TIME_ANY;
  string presence = PRESENCE_ANY;
  // Типы фильтров
  enum FilterType {FILTER_GROUP, FILTER_DATE, FILTER_TIME, FILTER_PRESENCE};
  // Константы фильтров
  typedef const char* strconst; //Тип для строковых констант
  static constexpr strconst GROUP_ANY = "*"; //Не фильтровать записи по группе
  static constexpr strconst DATE_ANY = "*"; //Не фильтровать записи по дате
  static constexpr strconst TIME_ANY = "*"; //Не фильтровать записи по времени
  static constexpr strconst PRESENCE_ANY = "*"; //Не фильтровать записи по присутствию/отсутствию студента
  static constexpr strconst PRESENCE_YES = "true"; //Фильтр записей по присутствию на занятии
  static constexpr strconst PRESENCE_NO = "false"; //Фильтр записей по отсутствию на занятии
  //Операторы и преобразования
  inline const string toString(bool skipWildcards = true) const; //Запись параметров фильтрации в одну строку
  const bool operator<(const TimeRecordFilters other) const; //Для сортировки в std::map();
  const bool operator==(const TimeRecordFilters other) const; //Проверка на равенство двух наборов фильтров
  //Формирование SQL-запросов и их частей
  static string SQLCondition(string filter, FilterType type); //Перевод фильтра в предикат SQL
  static inline string uniteSQLConditions(string filter, char delim, string op, FilterType); //Объединение предикатов
  string SQLQuery(); //Создание SQL-запроса для таблицы "timerecords" с учётом всех фильтров
};

typedef std::vector<TimeRecord> TimeRecords;
typedef map<TimeRecordFilters, TimeRecords> TimeCache;
typedef list<TimeRecordFilters> TimeCacheQueue;

class TimeRecordsRequestHandler: public CachedRequestHandler {
public:
  TimeRecordsRequestHandler(Session* dbSession, TimeRecordFilters filters);
  static bool cacheOutdated; //Данные в кэше устарели или отсутствуют
  bool cacheUpdate() override; //Обновить кэш списка вручную (true, если успешно)
  Array cacheArray() override; //Данные кэша в формате JSON
  Array cacheArray(TimeRecordFilters filter); //Данные по фильтру в формате JSON
  Object* getResponseObject() override; //Ответ на запрос списка групп
  //Параметры обработки запроса
  TimeRecordFilters filters;
  
private:
  static TimeCache cache; //Кэш записей по времени
  static TimeCacheQueue cacheOrder; //Очередь с порядком добавления элементов в кэш
  static const int CACHE_SIZE = 30; //Максимальное количество записей, которое может храниться в кэше
};
#endif

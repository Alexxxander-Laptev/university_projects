/// Обработчик запроса на записи о посещаемости (реализация)
#include "timerecords.hpp"
#include "agents/timerecords.hpp"
#include <sstream>
#include <Poco/JSON/Parser.h>
#include <Poco/Dynamic/Var.h>

//Вспомгательные функции
inline bool startsWith(string s, string begin) {
  //Проверка на совпадение начала строки s со строкой begin
  s.resize(begin.size()); //Выравниваем строки по длине
  return s == begin;
}

//Методы структур
Object TimeRecord::JSONObject() {
  Object obj;
  obj.set("id", id);
  obj.set("date", date);
  obj.set("time", time);
  obj.set("present", present);
  return obj;
}

typedef TimeRecordFilters::FilterType FilterType;
inline string TimeRecordFilters::uniteSQLConditions(string filter, char delim, string op, FilterType type) {
  istringstream ss(filter);
  string united = "("; //Объединённый предикат
  string sub; //Временная переменная для подфильтра
  while(getline(ss, sub, delim)) {
    if (united != "(") //Перед первым предикатом op не ставится
      united += op;
    united += SQLCondition(sub, type);
  }
  return united + ")";
}

string TimeRecordFilters::SQLCondition(string filter, FilterType type) {
  string param; //Сравниваемый параметр
  switch(type) {
  case FILTER_GROUP:
    param = "groups.name";
    break;
  case FILTER_DATE:
    param = "date";
    break;
  case FILTER_TIME:
    param = "time";
    break;
  case FILTER_PRESENCE:
    param = "presence";
    break;
  }
  //Предикаты "больше-меньше"
  for (string pred: {"<=", ">=", "<", ">"}) {
    if (startsWith(filter, pred)) {
      filter = filter.substr(pred.size());
      if (type != FILTER_PRESENCE)
	filter = "\'" + filter + "\'";
      return param + pred + filter; 
    }
  }
  //Предикат диапазона
  int betweenSep = filter.find('-');
  if (betweenSep > -1) {
    string rrange = filter.substr(betweenSep + 1);
    string lrange = filter.substr(0, betweenSep);
    if (type != FILTER_PRESENCE) {
	lrange = "\'" + lrange + "\'";
	rrange = "\'" + rrange + "\'";
    }
    return param + " BETWEEN " + lrange + " AND " + rrange;
  }
  //Предикаты, объединённые дизъюнкцией
  if (filter.find('|') != string::npos)
    return uniteSQLConditions(filter, '|', " OR ", type);
  //Предикаты, объединённые конъюнкцией
  if (filter.find('+') != string::npos)
    return uniteSQLConditions(filter, '+', " AND ", type);
  //Предикат одинарного равенства
  if (type != FILTER_PRESENCE)
    filter = "\'" + filter + "\'";
  return param + "=" + filter;
}

string TimeRecordFilters::SQLQuery() {
  string query = "SELECT studId, date, time, presence FROM students, groups, timerecords";
  query += " WHERE students.id = studId AND groups.id = groupId";
  if (group != GROUP_ANY)
    query += " AND " + SQLCondition(group, FILTER_GROUP);
  if (date != DATE_ANY)
    query += " AND " + SQLCondition(date, FILTER_DATE);
  if (time != TIME_ANY)
    query += " AND " + SQLCondition(time, FILTER_TIME);
  if (presence != PRESENCE_ANY)
    query += " AND " + SQLCondition(presence, FILTER_PRESENCE);
  query += ";";
  return query;
}

inline const string TimeRecordFilters::toString(bool skipWildcards) const {
  if (!skipWildcards) //Если разрешён вывод фильтров типа "*" (любое значение)
    return "group=" + group + "&date=" + date + "&time=" + time + "&presence=" + presence;
  string ret; //Возвращаемые данные
  static const string params[] = {"group", "date", "time", "presence"};
  const string* fields[] = {&group, &date, &time, &presence};
  for (int i = 0; i < 4; i++){
    const string field = *fields[i];
    if (field != "*") {
      if (!ret.empty())
	ret += "&";
      ret += params[i] + "=" + field;
    }
  }
  return ret;
}

const bool TimeRecordFilters::operator<(const TimeRecordFilters other) const {
  return this->toString() < other.toString();
}

const bool TimeRecordFilters::operator==(const TimeRecordFilters other) const {
  return (this->date == other.date) && (this->time == other.time) &&
    (this->group == other.group) && (this->presence == other.presence);
}

//Объявление статичных (static) членов класса
TimeCache TimeRecordsRequestHandler::cache;
TimeCacheQueue TimeRecordsRequestHandler::cacheOrder;
bool TimeRecordsRequestHandler::cacheOutdated = true;

//Конструктор класса
TimeRecordsRequestHandler::TimeRecordsRequestHandler(Session* dbSession, TimeRecordFilters filters): CachedRequestHandler(dbSession) {
  this->filters = filters;
};

//Собственные методы класса
Array TimeRecordsRequestHandler::cacheArray(TimeRecordFilters filter) {
  Array arr; //Массив для объектов JSON
  TimeRecords tr; //Записи о посещаемости
  try {
    tr = cache[filter];
  } catch (std::exception ex) {
    //Обновить кэш и повторно извлечь записи из него
    swap(this->filters, filter); //Временная замена
    cacheUpdate();
    swap(this->filters, filter);
    tr = cache[filter];
  }
  for (TimeRecord t: tr)
    arr.add(t.JSONObject());
  //Возврат JSON-строки
  return arr;
}

//Реализация виртуальных методов родительских классов
Array TimeRecordsRequestHandler::cacheArray() {
  using Poco::Dynamic::Var; //Динамический тип переменных
  Array arr; //Массив для объектов JSON
  for (auto cached: cache) {
    TimeRecordFilters f = cached.first;
    Object obj;
    obj.set("filters", f.toString());
    obj.set("data", cacheArray(f));
    arr.add(obj);
  }
  return arr;
}
bool TimeRecordsRequestHandler::cacheUpdate() {
  using namespace Poco::Data::Keywords;
  try {
    if (dbSession == nullptr)
	throw ConnectionFailedException("DB session is not specified");
    if (cacheOutdated) {
      //Очистка кэша от устаревших данных
      cache.clear();//TODO: сделать выборочную очистку
      cacheOrder.clear();
      time_t cachedTime = time(nullptr);
      cout << "INFO: Outdated cache clear on " << ctime(&cachedTime);
      cacheOutdated = false;
    }
    auto order = find(cacheOrder.begin(), cacheOrder.end(), filters);
    if (order != cacheOrder.end()) {
      //Результат уже есть в кэше, обновить его положение в очереди
      cacheOrder.erase(order);
      cacheOrder.push_back(filters);
    }
    else {
      if (cacheOrder.size() >= CACHE_SIZE) {
	//Очистка кэша от данных, к которым давно не обращались
	cache.erase(cacheOrder.front());
	cacheOrder.pop_front();
      }
      //Получение результатов из БД и добавление их в кэш
      TimeRecords tr;
      string query = filters.SQLQuery();
      Statement statement(*dbSession);
      TimeRecord t; //Временный объект для хранения данных о посещаемости
      statement << query, into(t.id), into(t.date), into(t.time),
	into(t.present), range(0, 1);
      while (!statement.done()) {
	statement.execute();
	tr.push_back(t);
      }
      cache[filters] = tr;
      assert(tr.size() == cache[filters].size());
      if (cacheOrder.size() == CACHE_SIZE - 1)
	cout << "WARNING: The time record cache is going to be overflowed. Old data will be erased until they are required again." << endl;;
      time_t cachedTime = time(nullptr);
      cacheOrder.push_back(filters);
      cout << "INFO: Cached time records for filters \'" << filters.toString() << "\' on " << ctime(&cachedTime);
    }
  } catch (Poco::Exception ex) {
    cerr << "ERROR: Time record cache update error!" << endl;
    cerr << ex.displayText() << endl;
    return false;
  }
  return true;
}

Object* TimeRecordsRequestHandler::getResponseObject() {
  static Array actions;
  static Object required;
  if (actions.size() == 0) {
    for (auto action: {"add", "alter", "remove"}) {
      actions.add(action);
      TimeRecordAgent tra(dbSession); //Для доступа к виртуальным методам
      Array props;
      for (auto prop: tra.requiredProperties())
	props.add(prop);
      if (action != "remove")
	props.add("present");
      required.set(action, props);
    }
  }
  string f = filters.toString();
  if (!f.empty())
    f.insert(0, "?");
  return responseObject(cacheArray(filters), actions, required, f);
}


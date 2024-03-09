///Базовый класс для агентов взаимодействия с базой данных (заголовок)
#include <Poco/Data/Session.h>
#include <Poco/Data/Statement.h>
#include <Poco/JSON/Object.h>
#include <Poco/Net/NetException.h> //Для вызова "сетевых" исключений из-под методов агента
#include <vector>
#ifndef HANDLERS_AGENTS_AGENT_HPP_INCLUDED
#define HANDLERS_AGENTS_AGENT_HPP_INCLUDED

using namespace std;
using namespace Poco::Data;
using namespace Poco::JSON;
using namespace Poco::Net;

class DBAgent {
  friend class ReqFactory;
public:
  //Конструкторы и деструктор класса
  DBAgent(Session* dbSession, const Object& defaults = Object());
  virtual ~DBAgent();
  //Параметры внесения изменений
  bool addIfNotExist = true; //При работе метода alter() добавлять новые записи, если они не существуют в БД
  bool ignoreIdleRemoval = true; //Считать попытки удаления несуществующих записей успешным удалением 
  Object defaults; //Значения свойств JSON-объектов по умолчанию
  //Виртуальные методы обработчика (при подаче аргументов через JSON-объекты)
  //Возвращаемые значения: true = операция прошла успешно, false = ошибка
  virtual bool add(const Object& obj) = 0; //Добавить запись
  virtual bool alter(const Object& obj) = 0; //Изменить запись
  virtual bool remove(const Object& obj) = 0; //Удалить запись
  virtual bool act(const string& method, const Object& obj); //Выполнить одно из выше объявленных действий, указанное в строке method
  //Методы проверки целостности и дополнения данных
  virtual bool complete(Object& obj); //Дополняет объект недостающими данными (true, если данных по умолчанию хватило для заполнения)
  bool full(const Object& obj); //Проверяет полноту объекта без дополнения
  //Возращаемые параметры объекта
  virtual const std::vector<string> requiredProperties(); //Список необходимых свойств JSON-объекта
  Session* getDBSession(); //Вернуть dbSession
protected:
  Session* dbSession = nullptr; //Сессия связи с БД
  Statement* sql = nullptr; //Общий объект выражения SQL
  void prepare(); //Подготовиться к следующей транзакции
};
#endif

/// Обработчик HTTP-запросов со связанным агентом взаимдействия с базой данных (реализация)
#include "agent.hpp"
#include <Poco/Data/DataException.h>
#include <Poco/JSON/Parser.h>
#include <Poco/Dynamic/Var.h>

using namespace Poco::JSON;
using Poco::Dynamic::Var;
extern Parser parser;

//Вспомогательные функции
void fillLackingValues(Object& a, const Object& b) {
  //Взять из объекта b те значения, которых нет в объекте a
  for (auto it = b.begin(); it != b.end(); it++) {
    if (!a.has(it->first))
      a.set(it->first, it->second);
  }
}

//Конструкторы и деструктор обработчика запросов
AgentRequestHandler::AgentRequestHandler(DBAgent* agent) {
  setAgent(agent);
}

AgentRequestHandler::~AgentRequestHandler() {
  deleteAgent();
}

//Работа с агентами
DBAgent* AgentRequestHandler::setAgent(DBAgent* agent) {
  deleteAgent(); //Удалить старого агента из памяти
  this->agent = agent;
  return agent;
}

DBAgent* AgentRequestHandler::getAgent() {
  return agent;
}

void AgentRequestHandler::deleteAgent() {
  if (agent != nullptr)
    delete agent;
}

//Стандартный обработчик HTTP-запросов с применением агентов
void AgentRequestHandler::badRequest(HTTPServerResponse& res, const string& error) {
  //Отправка ошибки некорректного запроса (400) с указанием ошибки синтаксиса
  res.setStatusAndReason(HTTPResponse::HTTP_BAD_REQUEST);
  ostream& resBody = res.send();
  if (error != "") {
    res.setContentType("text/plain");
    resBody << "Bad request with the following " << error; //...Exception:...
    resBody << endl;
    //Отправка предупреждения в консоль сервера
    cerr << "ERROR: The request is bad (400), so the handler threw " << error; //...Exception...
    cerr << endl;
  }
  resBody.flush();
}

void AgentRequestHandler::handleRequest(HTTPServerRequest& req, HTTPServerResponse& res) {
  try {
    string method = req.getMethod();
    if (method == HTTPRequest::HTTP_GET)
      return; //Данный обработчик не обрабатывает GET-запросы
    if (agent == nullptr)
      throw ConnectionFailedException("Agent is not set");

    //Получение тела запроса
    istream& reqBody = req.stream();
    string reqBodyStr;
    Var result; //Результат парсинга JSON из тела запроса
    try {
      while (!reqBody.eof()) {
	string s;
	reqBody >> s;
	reqBodyStr += s;
      }
      result = parser.parse(reqBodyStr);
    } catch (JSONException ex) {
      badRequest(res, ex.displayText());
      cerr << "Full request body:" << endl << reqBodyStr << endl;
      return;
    }
     
    Object::Ptr resultObj = result.extract<Object::Ptr>();

    //Получение парамтеров по умолчанию (опционально)
    if (getDefaults) {
      Object defaults;
      if (resultObj->has("defaults"))
	defaults = *resultObj->getObject("defaults");
      //Перенастройка агента под полученные параметры)
      if (defaults.size() > 0)
	fillLackingValues(agent->defaults, defaults);
    }
    //Определние выполняемого действия по типу и содержанию запроса
    string action = "alter"; //Выполняемое действие
    bool isDELETE = (method == HTTPRequest::HTTP_DELETE);
    if (isDELETE) {
      action = "remove"; //Для DELETE-запроса всегда равно "remove"
    } else if (resultObj->has("action")) {
      action = resultObj->getValue<string>("action");
    }
    
    if (!(action == "add" || action == "remove"))
      action = "alter"; //Исправление action на значение по умолчанию

    //Выполнение выбранного действия (act)
    Array::Ptr data = resultObj->getArray("data");
    size_t fails = 0; //Счётчик невыполненных действий
    for (Var item: *data) {
      Object::Ptr obj = item.extract<Object::Ptr>();
      try {
	bool success = agent->act(action, *obj);
	if (!success) fails++;
      }
      catch (Poco::Exception ex) {
	cerr << ex.displayText() << endl;
	fails++;
      }
    } 
    
    //Определние статуса ответа
    typedef HTTPResponse::HTTPStatus Status;
    Status status = HTTPResponse::HTTP_OK; //Статус ответа по умолчанию
    if (action == "add") {
      if (fails == 0)
	status = HTTPResponse::HTTP_CREATED;
      else
	status = HTTPResponse::HTTP_ACCEPTED;
    }
    else if (action == "remove") {
      if (fails == 0 && !isDELETE)
	status = HTTPResponse::HTTP_NO_CONTENT;
    }
    else //status == "alter"
      if (fails != 0)
	status = HTTPResponse::HTTP_ACCEPTED;

    //Отправка ответа
    res.setStatusAndReason(status);
    res.setContentType("text/plain");
    ostream& resBody = res.send(); //Поток тела ответа
    ostringstream failString; //Строковый поток с числом ошибок выполнения запроса
    failString << fails << " fail" << (fails != 1 ? "s": ""); 
    if (fails == 0)
      resBody << "Success!" << endl;
    else
      resBody << failString.str() << endl;
    resBody.flush(); //Завершение отправки тела ответа
    cout << "INFO: Request done with " << failString.str() << endl;
  } catch (Poco::Exception ex) {
    cerr << "Time altering (agent) request handling error!" << endl;
    cerr << ex.displayText() << endl;
    //Отправка ошибки 501
    res.setStatusAndReason(HTTPResponse::HTTP_INTERNAL_SERVER_ERROR);
    res.send().flush();
  }
}

void DBAgent::prepare() {
  sql->reset(*dbSession);
}

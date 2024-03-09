/// Обработчик HTTP-запросов со связанным агентом взаимдействия с базой данных (заголовок)
#include "agents/agent.hpp" //Полиморфный шаблон для всех агентов
#include <Poco/Net/HTTPRequestHandler.h>
#include <Poco/Net/HTTPServerRequest.h>
#include <Poco/Net/HTTPServerResponse.h>
#include <Poco/Data/Session.h>
#include <Poco/JSON/Object.h>
#ifndef HANDLERS_AGENT_HPP_INCLUDED
#define HANDLERS_AGENT_HPP_INCLUDED

using namespace std;
using namespace Poco::Net;
using Poco::Data::Session;
using Poco::JSON::Object;

class AgentRequestHandler: public HTTPRequestHandler{
  typedef HTTPServerRequest Request;
  typedef HTTPServerResponse Response;
public:
  //Конструкторы и деструкторы класса
  AgentRequestHandler(DBAgent* agent);
  ~AgentRequestHandler();
  //Управление агентами
  DBAgent* setAgent(DBAgent* agent); //Назначить уже существующего агента
  DBAgent* getAgent(); //Получить указатель на текущего агента
  void deleteAgent(); //Удалить агента
  //Параметры обработки запроса
  bool getDefaults = true; //Получать из запроса значения по умолчанию
protected:
  DBAgent* agent = nullptr; //Агент обработчика запросов
  //Обработка HTTP-запросов
  void badRequest(Response& res, const string& error = ""); //Ошибка некорректного запроса
  void handleRequest(Request& req, Response& res); //Обработка запроса
};
#endif

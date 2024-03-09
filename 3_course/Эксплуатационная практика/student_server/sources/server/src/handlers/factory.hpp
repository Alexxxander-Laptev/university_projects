/// Фабрика обработчиков HTTP-запросов (заголовок)
#include <Poco/Net/HTTPRequestHandlerFactory.h>
#include <Poco/Data/Session.h>
#include <string>
#include <map>
#ifndef HANDLERS_FACTORY_HPP_INCLUDED
#define HANDLERS_FACTORY_HPP_INCLUDED

using namespace std;
using namespace Poco::Net;
using namespace Poco::Data;

class ReqFactory: public HTTPRequestHandlerFactory {
public:
  ReqFactory(Session* dbSession);
private:
  Session* dbSession = nullptr; //Общий сеанс связи с базой данных
  HTTPRequestHandler* createRequestHandler(const HTTPServerRequest& req) override; //Метод-фабрикант обработчиков запросов
};
#endif

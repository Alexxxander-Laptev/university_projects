/// Абстрактный обработчик HTTP-запроса с кэшированием (заголовок)
#include <Poco/Net/HTTPRequestHandler.h>
#include <Poco/Net/HTTPServerRequest.h>
#include <Poco/Net/HTTPServerResponse.h>
#include <Poco/Data/Session.h>
#include <Poco/JSON/Array.h>
#include <Poco/JSON/Object.h>
#include <ctime> //Для фиксации времени тех или иных событий в дочерних классах
#ifndef HANDLERS_CACHED_HPP_INCLUDED
#define HANDLERS_CACHED_HPP_INCLUDED

using namespace std;
using namespace Poco::Data;
using namespace Poco::Net;
using namespace Poco::JSON;

/*ПРИМЕЧАНИЕ: Все новые методы, кроме конструктора класса, а также
наследуемый метод handleRequest() являются чисто виртуальными (pure virtual)
и должны быть перезаписаны дочерними классами для их полной реализации.*/
class CachedRequestHandler: public HTTPRequestHandler {
public:
  CachedRequestHandler(Session* dbSession);
  static Session* dbSession; //Сеанс связи с БД
  virtual Array cacheArray() = 0; //Данные из кэша в формате JSON-массив
  virtual Object* getResponseObject() = 0; //Вернуть JSON-объект для ответа на запрос
protected:
  virtual bool cacheUpdate() = 0; //Обновить кэш (true, если успешно)
  static Object* responseObject(const Array& data, const Array& actions, const Object& requiredProperties, const string& filter); //Сгенерировать JSON-объект для ответа на запрос
  static void respondError(HTTPServerResponse& res, HTTPResponse::HTTPStatus status); //Выдать клиенту ошибку запроса
  virtual void handleRequest(HTTPServerRequest& req, HTTPServerResponse& res); //Обработка запросов (задан стандартный способ)
};
#endif

/// Абстрактный обработчик HTTP-запроса с кэшированием (реализация)
#include "cached.hpp"

// Определние статичных (static) членов класса
Session* CachedRequestHandler::dbSession = nullptr;

// Определение конструктора класса
CachedRequestHandler::CachedRequestHandler(Session* dbSession) {
  this->dbSession = dbSession;
}

Object* CachedRequestHandler::responseObject(const Array& data, const Array& actions, const Object& requiredProperties, const string& filter){
  Object* obj = new Object();
  obj->set("data", data); //Данные ответа
  obj->set("actions", actions); //Список доступных действий с данными
  obj->set("requiredProperties", requiredProperties); //Список аргументов, требуемых для того или иного действия (или для всех сразу)
  obj->set("timeRecords", "/timerecords" + filter); //Ссылка на таблицу посещаемости по данному запросу (с необходимыми фильтрами)
  return obj;
}

typedef HTTPResponse::HTTPStatus Status;
void CachedRequestHandler::respondError(HTTPServerResponse& res, Status status) {
  res.setStatusAndReason(status);
  ostream& resBody = res.send();
  resBody << status << " - " << res.getReason() << endl;
  resBody.flush();
}

void CachedRequestHandler::handleRequest(HTTPServerRequest& req, HTTPServerResponse& res) {
  try {
    cacheUpdate(); //Обновление кэша из базы данных
    //Отправка ответа в формате JSON
    res.setContentType("application/json");
    ostream& resBody = res.send();
    cout << "INFO: Obtaining the requested data from the cache..." << endl;
    Object* resObj = getResponseObject();
    resObj->stringify(resBody);
    delete resObj;
    resBody << endl; //Для "крассивого" вывода в консольных программах типа curl
    resBody.flush();
    cout << "INFO: Request done!" << endl;
  } catch (Poco::Exception ex) {
    //Ошибка формирования ответа на запрос (сервер отсылает ошибку 500)
    respondError(res, HTTPResponse::HTTP_INTERNAL_SERVER_ERROR);
    cerr << "Request handling error!" << endl;
    cerr << ex.displayText() << endl;
  }
}

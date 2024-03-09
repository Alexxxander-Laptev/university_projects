#include <Poco/Util/ServerApplication.h> //Надстройка над main() для серверов
#include <Poco/Data/PostgreSQL/Connector.h>
#include <Poco/Net/HTTPServer.h>
#include <Poco/JSON/Parser.h>
#include <iostream>
#include "handlers/factory.hpp"

using namespace std;
using namespace Poco::Data;
using namespace Poco::Util;

class MyServer: public ServerApplication {
protected:
  int main(const vector<string>&) override {
    try {
      //Подключение к серверу PostgreSQL
      cout << "Connecting to the database...";
      PostgreSQL::Connector::registerConnector();
      string connStr = "host=127.0.0.1 user=postgres password=postgres dbname=studentdb"; 
      Session psql(PostgreSQL::Connector::KEY, connStr);
      cout << "\tDONE!" << endl;
      //Инициализация HTTP-сервера
      cout << "Initializing the HTTP server...";
      auto factory = new ReqFactory(&psql);
      auto srvParams = new HTTPServerParams(); //Параметры сервера
      srvParams->setTimeout(Poco::Timespan(5, 0));
      HTTPServer srv(factory, ServerSocket(80), srvParams); //Сервер
      cout << "\tDONE!" << endl;
      //Запуск сервера
      cout << "Starting up the server...";
      srv.start();
      cout << "\tDONE!" << endl;
      //Ожидание сигнала завершения работы
      cout << "Press Ctrl+C to kill the server" << endl;
      waitForTerminationRequest();
      //Отключение сервера
      cout << "\nShutting down the server...";
      srv.stop();
      cout << "\tDONE!" << endl;
    }
    catch (Poco::Exception ex) {
      string text = ex.displayText();
      cerr << endl << text << endl;
      if (text == "Exception: Permission denied") {
	//Программа запущена с недостаточным количеством прав для запуска сервера
	cerr << "Ensure you run the program under the root user (sudo !!)" << endl;
      }
      return 1;
    }
    return 0;
  }
};

Poco::JSON::Parser parser; //Парсер JSON (объявлен для других .cpp-файлов)

int main(int argc, char** argv) {
  MyServer app;
  return app.run(argc, argv);
}

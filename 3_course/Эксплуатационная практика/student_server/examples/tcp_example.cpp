#include <iostream>
#include <Poco/Net/TCPServer.h>
using namespace std;
using namespace Poco::Net;

class EchoConnection: public TCPServerConnection {
  //Отработчик соединений
public:
  EchoConnection(const StreamSocket& s): TCPServerConnection(s) {
    //Конструктор обработчика соединения
  }
  void run() {
    //Обработка соединения
    StreamSocket& ss = socket();
    try {
      char buffer[256]; //Буфер данных
      int n; //Размер поступивших данных
      for(;;) {
	n = ss.receiveBytes(buffer, sizeof(buffer));
	if (n <= 0) //Данные не поступили (конец обмена)
	  break;
	cout << "Server recieved data: " << string(buffer, n) << endl;
	ss.sendBytes(buffer, n); //Отправить данные обратно
      }
    } catch (Poco::Exception& ex) {
      cerr << "EchoConnection: " << ex.displayText() << endl;
    }
  }
};

//Фабрика соединений
auto ecFactory = new TCPServerConnectionFactoryImpl<EchoConnection>();
TCPServer srv(ecFactory); //Сервер

void client() {
  //Моделирование поведения со стороны клиента
  int port = srv.socket().address().port();
  SocketAddress sa("localhost", port);
  StreamSocket ss(sa);
  //Отправка данных
  string data = "Hello world!";
  ss.sendBytes(data.data(), (int) data.size());
  //Приём данных
  char buffer[256];
  int n = ss.receiveBytes(buffer, sizeof(buffer));
  cout << "Client recieved data: " << string(buffer, n) << endl;
}

int main() {
  srv.start();
  client();
  srv.stop();
  return 0;
}

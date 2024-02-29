#include <iostream>
#include <Poco/Data/Session.h>
#include <Poco/Data/PostgreSQL/Connector.h>

using namespace std;
using namespace Poco::Data;
using namespace Poco::Data::Keywords;

struct ResRow {
  int id;
  string value;
};

int main() {
  try {
    //Подключение к серверу PostgreSQL
    PostgreSQL::Connector::registerConnector();
    string connStr = "host=127.0.0.1 user=postgres password=postgres dbname=studentdb"; 
    Session psql(PostgreSQL::Connector::KEY, connStr);
  
    //Вывод данных из таблицы test
    Statement query(psql);
    ResRow result;
    query << "SELECT * FROM test ORDER BY id;", //Запрос
      into(result.id), into(result.value), //Переменные для записи
      range(0, 1); //Итерация при следующем обращении
    //Содержание таблицы
    while (!query.done()){
      query.execute();
      cout << result.id << '\t' << result.value << endl;
    }
    psql.close();
  } catch (Poco::Exception ex) {
    cerr << ex.displayText() << endl;
    return 1;
  }
  return 0;
}

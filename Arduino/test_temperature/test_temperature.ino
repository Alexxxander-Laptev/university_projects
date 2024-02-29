#include "max6675.h"

int thermoDO = 2;  //он же SO
int thermoCS = 3;
int thermoCLK = 4;  //он же SCK

MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);

int vccPin = 5;  //пин для питания
int gndPin = 6;  //пин для земли

float temp;

void setup() {
  Serial.begin(9600);  //задаем скорость передачи данных и инициируем последовательное соединение
  //активируем питание и землю
  pinMode(vccPin, OUTPUT); digitalWrite(vccPin, HIGH);
  pinMode(gndPin, OUTPUT); digitalWrite(gndPin, LOW);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println("MAX6675 test");
  //ждем стабилизации чипа MAX
  delay(500);
  temp = thermocouple.readCelsius();
}

void loop() {
  //Выводим показания в монитор порта
  if ((thermocouple.readCelsius() <= temp + temp * 0.1) and (thermocouple.readCelsius() >= temp - temp * 0.1)){
    Serial.print("C = ");
    Serial.print(thermocouple.readCelsius());
    Serial.print(";   F = ");
    Serial.println(thermocouple.readFahrenheit());
    delay(300);
  }
  else
    Serial.print("Cool the device!\n");
    digitalWrite(LED_BUILTIN, HIGH);
    delay(300);
    digitalWrite(LED_BUILTIN, LOW);
    delay(300);
}

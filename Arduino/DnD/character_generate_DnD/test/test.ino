#include <Wire.h> // добавляем необходимые библиотеки
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7 );

#define BTN_R 1
#define BTN_U 2
#define BTN_D 3
#define BTN_L 4
#define BTN_S 5
#define BTN_NONE 10
int i = 0;
int j = 0;
int characteristics_pers[] = {"Strong:", "Constitution", "Dexterity:", "Intelligence", "Wisdom", "Charisma"};
int rand_roll = 0;
char* race[] = {"People", "Dwarves", "Elves", "Gnomes", "Halflings", "Genasi", "Tieflings", "Aasimar", "Eldraine"};
char* class_pers[] = {"Priest", "Warrior", "Robber", "Magician"};
char* header[7] = {"t", "o", "r", " ", "D", "n", "D"};
unsigned long timing; // Переменная для хранения точки отсчета

int clickButton() {
  int keyAnalog = analogRead(A0);
  
  if (keyAnalog < 99) {
    // Значение меньше 100 – нажата кнопка right
    return BTN_R;
  } else if (keyAnalog < 200) {
    // Значение больше 100 (иначе мы бы вошли в предыдущий блок результата сравнения, но меньше 200 – нажата кнопка UP
    return BTN_U;
  } else if (keyAnalog < 400) {
    // Значение больше 200, но меньше 400 – нажата кнопка DOWN
    return BTN_D;
  } else if (keyAnalog < 600) {
    // Значение больше 400, но меньше 600 – нажата кнопка LEFT
    return BTN_L;
  } else if (keyAnalog < 800) {
    // Значение больше 600, но меньше 800 – нажата кнопка SELECT
    return BTN_S;
  } else {
    // Все остальные значения (до 1023) будут означать, что нажатий не было
    return BTN_NONE;
  }
}

void mainText() {
  int btnSel = clickButton();

  lcd.setCursor(0, 1);
  lcd.print("Press 'SELECT'");
  lcd.home();
  lcd.print("Character genera");
  for (timing = 0; millis() - timing <= 500; millis()) {
    
  }
//  delay(500);

  // Включаем автоматическое смещение текста:
  lcd.autoscroll();
  for (int j = 0; j < 7; j++) {
    lcd.print(header[j]);
    for (int k = timing; millis() - k <= 1000; millis()) {
      timing = millis();
    }
//    delay(500);
  }
  // Выключаем «автосмещение»:
  lcd.noAutoscroll();

  switch (btnSel){
    case BTN_S:
      lcd.clear();
      while(1) {
        lcd.home();
        lcd.print("test");
      }
      break;
    default:
      break;
  }
  lcd.clear();
}

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
/* 
 В этом месте начинается выполнение аналога delay()
 Вычисляем разницу между текущим моментом и ранее сохраненной точкой отсчета.
 Если разница больше нужного значения, то выполняем код. 
 Если нет - ничего не делаем 
*/
//  for (timing = 0; millis() - timing <= 2000; millis()) {
//    lcd.home();
//  }
  mainText();
//  lcd.clear();
//  if (millis() - timing == 1000){ // Вместо 10000 подставьте нужное вам значение паузы 
//    timing = millis();
//    text();
//  }
//  if (millis() - timing == 2000){ // Вместо 10000 подставьте нужное вам значение паузы 
//    timing = millis();
//    lcd.clear();
//  }
}
//void setup()
//{
//  // create a new custom character
//  lcd.createChar(0, customChar);
//  
//  // set up number of columns and rows
//  lcd.begin(16, 2);
//
//  lcd.setCursor(15, 0);
//  // print the custom char to the lcd
//  lcd.print(char(0));
//}
//
//void loop()
//{
//  
//}

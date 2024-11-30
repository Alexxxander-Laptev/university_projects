#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7); // Пины для подключения lcd-дисплея

#define BTN_R 1
#define BTN_U 2
#define BTN_D 3
#define BTN_L 4
#define BTN_S 5
#define BTN_NONE 10

int i = 0;
int j = 0;
int k = 0;
int sel;
int characteristics[] = {0, 0, 0, 0, 0, 0, 0, 0};
char* characteristicsPers[] = {"Race: ", "Class: ", "Str: ", "Con: ", "Dex: ", "Int: ", "Wis: ", "Cha: ", "HP: ", "AC: "};
char* racePers[] = {"Human", "Dwarf", "Elf", "Half-orc", "Gnome", "Goliath", "Halfling", "Genasi", "Tiefling", "Aasimar", "Eladrin", "Dragonborn"};
char* classPers[] = {"Bard", "Barbarian", "Fighter", "Wizard", "Druid", "Cleric", "Artificer", "Warlock", "Monk", "Paladin", "Rogue", "Ranger", "Sorcerer"};
char* pers[] = {"", ""};

//Стрелка вврех
byte arrowUp[8] = {
  0b00000,
  0b00000,
  0b00100,
  0b01110,
  0b11111,
  0b00000,
  0b00000,
  0b00000
};

//Стрелка вниз
byte arrowDown[8] = {
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b01110,
  0b00100,
  0b00000,
  0b00000
};

//Обработка нажатой клавици
int clickButton() {
  int keyAnalog = analogRead(A0);
  
  if (keyAnalog < 100) {
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

//Текст в главном окне
void mainText() {
  int roll;
  int randRoll = 0;
  int characteristic;
  
  lcd.setCursor(0, 1);
  lcd.print("Press the 'SELECT' button");
  lcd.home();
  lcd.print("Character generator DnD");
  delay(500);

  int btnSel = 0;
  for (int j = 0; j < 9; j++) {
    btnSel = clickButton();
    if (btnSel == 5) {
      break;
    }
    lcd.scrollDisplayLeft();
    delay(500);
  }

  switch (btnSel){  //Действия при нажатии кнопки SELECT
    case BTN_S:
      randomSeed(millis()); // Генерируем псевдослучайное число (каждый раз различное)
      for (int i = 0; i < 6; i++) { //Определяем значение для характеристики
        roll = 6;
        characteristic = 0;
        for (int j = 0; j < 4; j++) { //Для определения одной характеристики надо провести 6 бросков
          randRoll = random(1, 7);  //Симулируем бросок игральной кости
          if (randRoll < roll) {  //Осуществляем поиск минимального значения среди выброшенных
            roll = randRoll;
            characteristic += randRoll;
          }
          else
          {
            characteristic += randRoll;
          }
        }
        characteristics[i] = characteristic - roll; //Отбрасываем наименьшее значение
      }
      delay(500);
      lcd.clear();
      while(true) {
        lcd.home();
        genRacePers();  //Вызов функции для выбора расы
      }
      break;
    default:
      break;
  }
  lcd.clear();
}

//Выбор расы персонажа
void genRacePers() {
  if(i == 0) {
    lcd.print("Select race:");
    lcd.setCursor(0, 1);
    lcd.print(racePers[i]);
    lcd.createChar(2, arrowDown);
    lcd.setCursor(15, 1);
    lcd.print(char(2));
  }
  else if(i == 11) {
    lcd.print("Select race:");
    lcd.setCursor(0, 1);
    lcd.print(racePers[i]);
    lcd.createChar(1, arrowUp);
    lcd.setCursor(15, 0);
    lcd.print(char(1));
  }
  else {
    lcd.print("Select race:");
    lcd.setCursor(0, 1);
    lcd.print(racePers[i]);
    lcd.createChar(1, arrowUp);
    lcd.setCursor(15, 0);
    lcd.print(char(1));
    lcd.createChar(2, arrowDown);
    lcd.setCursor(15, 1);
    lcd.print(char(2));
  }
  delay(150);

  int btnRacePers = clickButton();
  switch (btnRacePers){
    case BTN_R:
      lcd.clear();
      i++;
      if (i > 11)
        i--;
      break;
    case BTN_U:
      lcd.clear();
      i--;
      if (i < 0)
        i++;
      break;
    case BTN_D:
      lcd.clear();
      i++;
      if (i > 11)
        i--;
      break;
    case BTN_L:
      lcd.clear();
      i--;
      if (i < 0)
        i++;
      break;
    case BTN_S:
      pers[0] = racePers[i];  //Запоминаем выбранную расу
      lcd.clear();
      while(true) {
        lcd.home();
        genClassPers(); //Вызываем функцию выбора класса
      }
      break;
    default:
      break;
  }
  lcd.clear();
}

//Функция выбора класса персонажа
void genClassPers() {
  if(j == 0) {
    lcd.print("Select class:");
    lcd.setCursor(0, 1);
    lcd.print(classPers[j]);
    lcd.createChar(2, arrowDown);
    lcd.setCursor(15, 1);
    lcd.print(char(2));
  }
  else if(j == 12) {
    lcd.print("Select class:");
    lcd.setCursor(0, 1);
    lcd.print(classPers[j]);
    lcd.createChar(1, arrowUp);
    lcd.setCursor(15, 0);
    lcd.print(char(1));
  }
  else {
    lcd.print("Select class:");
    lcd.setCursor(0, 1);
    lcd.print(classPers[j]);
    lcd.createChar(1, arrowUp);
    lcd.setCursor(15, 0);
    lcd.print(char(1));
    lcd.createChar(2, arrowDown);
    lcd.setCursor(15, 1);
    lcd.print(char(2));
  }
  delay(150);

  int btnClassPers = clickButton();
  switch (btnClassPers){
    case BTN_R:
      lcd.clear();
      j++;
      if (j > 12)
        j--;
      break;
    case BTN_U:
      lcd.clear();
      j--;
      if (j < 0)
        j++;
      break;
    case BTN_D:
      lcd.clear();
      j++;
      if (j > 12)
        j--;
      break;
    case BTN_L:
      lcd.clear();
      j--;
      if (j < 0)
        j++;
      break;
    case BTN_S:
      pers[1] = classPers[j]; //Запоминаем выбранный класс
      lcd.clear();
      while(true) {
        lcd.home();
        charactPers();  //Вызываем функцию для просмотра сгенерированных характеристик
      }
      break;
    default:
      break;
  }
  lcd.clear();
}

//Функция для просмотра сгенерированных характеристик
void charactPers() {
  int HP;
  int AC;

  //Определяем количество хит-поинтов персонажа
  if ((pers[1] == classPers[0]) || (pers[1] == classPers[4]) || (pers[1] == classPers[5]) || (pers[1] == classPers[6]) || (pers[1] == classPers[7]) || (pers[1] == classPers[8]) || (pers[1] == classPers[10])) {
    HP = 8 + floor((characteristics[1] - 10) / 2);
  }
  else if (pers[1] == classPers[1]) {
    HP = 12 + floor((characteristics[1] - 10) / 2);
  }
  else if ((pers[1] == classPers[2]) || (pers[1] == classPers[9]) || (pers[1] == classPers[11])) {
    HP = 10 + floor((characteristics[1] - 10) / 2);
  }
  else {
    HP = 6 + floor((characteristics[1] - 10) / 2);
  }
  characteristics[6] = HP;

  //Определяем класс защиты персонажа
  AC = 10 + floor((characteristics[2] - 10) / 2);
  characteristics[7] = AC;
  
  if(k == 0) {
    lcd.print("Characteristics:");
    lcd.setCursor(0, 1);
    lcd.print(characteristicsPers[k]);
    lcd.print(pers[k]);
    lcd.createChar(2, arrowDown);
    lcd.setCursor(15, 1);
    lcd.print(char(2));
  }
  else if(k == 1) {
    lcd.print("Characteristics:");
    lcd.setCursor(0, 1);
    lcd.print(characteristicsPers[k]);
    lcd.print(pers[k]);
    lcd.createChar(1, arrowUp);
    lcd.setCursor(15, 0);
    lcd.print(char(1));
    lcd.createChar(2, arrowDown);
    lcd.setCursor(15, 1);
    lcd.print(char(2));
  }
  else if(k == 9) {
    lcd.print("Characteristics:");
    lcd.setCursor(0, 1);
    lcd.print(characteristicsPers[k]);
    lcd.print(characteristics[k - 2]);
    lcd.createChar(1, arrowUp);
    lcd.setCursor(15, 0);
    lcd.print(char(1));
  }
  else {
    lcd.print("Characteristics:");
    lcd.setCursor(0, 1);
    lcd.print(characteristicsPers[k]);
    lcd.print(characteristics[k - 2]);
    lcd.createChar(1, arrowUp);
    lcd.setCursor(15, 0);
    lcd.print(char(1));
    lcd.createChar(2, arrowDown);
    lcd.setCursor(15, 1);
    lcd.print(char(2));
  }
  delay(150);

  int btnCharPers = clickButton();
  switch (btnCharPers){
    case BTN_R:
      lcd.clear();
      k++;
      if (k > 9)
        k--;
      break;
    case BTN_U:
      lcd.clear();
      k--;
      if (k < 0)
        k++;
      break;
    case BTN_D:
      lcd.clear();
      k++;
      if (k > 9)
        k--;
      break;
    case BTN_L:
      lcd.clear();
      k--;
      if (k < 0)
        k++;
      break;
    default:
      break;
  }
  lcd.clear();
}

void setup() {
  lcd.begin(16, 2); // Инициализация текстового дисплея 16х2
}

void loop() {
  mainText(); //Вызов функции для отображения текста на главном экране
}

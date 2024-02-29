#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <conio.h>

using namespace std;

void readFile(vector <string> repeatText)
{
	
    system("mode con cols=80 lines=24");    //  Задаем размер консольного окна

    int numberKey;

    string s;
    for (size_t firstDisplay = 0; firstDisplay < 23; firstDisplay++)
    {
        s = repeatText[firstDisplay];
        cout << s.substr(0, 80) << endl;
    }

    for (size_t countString = 0; countString < repeatText.size() - 22; countString++)
    {
        numberKey = _getch();
        if (numberKey == 27)    //  Завершаем по нажатию Esc
            return;
        numberKey = _getch();
        system("cls");  //  Очищаем дисплей
        switch (numberKey)
        {
        case 80:
            // Нажатие стрелки вниз
            if (countString == repeatText.size() - 24)  //  Если это последний блок
            {
                cout << countString << endl;
                for (size_t firstDisplay = countString; firstDisplay < countString + 24; firstDisplay++)
                {
                    // Выводим строки блоками по 23 - количество строк в окне (минус одна пустая)
                    s = repeatText[firstDisplay];
                    cout << s.substr(0, 80) << endl;
                }
                countString--;
            }
            else if (countString == 0)  //  Если это самый первый блок
            {
                for (size_t firstDisplay = countString; firstDisplay < countString + 24; firstDisplay++)
                {
                    s = repeatText[firstDisplay];
                    cout << s.substr(0, 80) << endl;
                }
            }
            else    //  Все остальные блоки
            {
                countString++;
                for (size_t firstDisplay = countString; firstDisplay < countString + 23; firstDisplay++)
                {
                    s = repeatText[firstDisplay];
                    cout << s.substr(0, 80) << endl;
                }
                countString--;
            }
            break;
        case 72:
            // Нажатие стрелки вверх
            if (countString == 0)   //   Первый блок
            {
                for (size_t firstDisplay = countString; firstDisplay < countString + 23; firstDisplay++)
                {
                    s = repeatText[firstDisplay];
                    cout << s.substr(0, 80) << endl;
                }
                countString--;
            }
            else    //  Все сотальные блоки
            {
                countString--;
                for (size_t firstDisplay = countString; firstDisplay < countString + 23; firstDisplay++)
                {
                    s = repeatText[firstDisplay];
                    cout << s.substr(0, 80) << endl;
                }
                countString--;
            }
            break;
        default:
            break;
        }
    }
}


void searchTextInFile(vector <string> repeatText)
{
    cout << "Find text: ";
    string findText;
    cin >> findText;

    for (size_t countString = 0; countString < repeatText.size(); countString++)
    {
        string s = repeatText[countString];
        int resultFind = 0;

        for (resultFind = s.find(findText, resultFind++); resultFind != string::npos; resultFind = s.find(findText, resultFind + 1))
            // Находим все совпадения подстроки для каждого элемента вектора
            cout << "Номер строки: " << countString + 1 << " Номер элемента: " << resultFind + 1 << endl;
    }
}


int main()
{
	setlocale(0, "");

	int number;
	string filename = "test.txt";
	do
	{
		cout << "Введите номер задания, которое надо выполнить:" << endl;
		cout << "1. Просмотр текстового файла." << endl;
		cout << "2. Поиск слова/фразы в текстовом файле." << endl;

		cin >> number;
	} while (number < 1 or number > 2);

    char buffer[2048];
    vector <string> repeatText;
    ifstream inputFile(filename);
	if (!inputFile.is_open())
	{
		cout << "File not found" << endl;
	}
	else
	{
        while (!inputFile.eof())
        {
            // Проходимся по файлу для подсчета количства строк
            // Каждую новую строку добавляем в вектор
            inputFile.getline(buffer, 2048, '\n');
            repeatText.push_back(buffer);
        }
    }
    inputFile.close();

	switch (number)
	{
	case 1:
		readFile(repeatText);
		break;
	case 2:
		searchTextInFile(repeatText);
		break;
	default:
		break;
	}
	system("pause");

	return 0;
}
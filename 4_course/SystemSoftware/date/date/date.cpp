#include <iostream>
#include <string>
#include <conio.h>
#include <vector>
#include <chrono>
#include <fstream>
#pragma warning(disable : 4996) //_CRT_SECURE_NO_WARNINGS

using namespace std;

void readFile(string filename)
{
    char buffer[2048];
    vector <string> text;
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
            text.push_back(buffer);
        }
    }
    inputFile.close();

    for (int i = 0; i < text.size(); i++)
    {
        cout << text.at(i) << endl;
    }
}

string formatingString(string temp, string argument, vector <string> formatVariant)
{
    auto timeNow = chrono::zoned_time{ chrono::current_zone(), chrono::system_clock::now() };

    if (argument == formatVariant.at(0))
    {
        temp += format("{0:%%}", timeNow);
    }
    else if (argument == formatVariant.at(1))
    {
        temp += format("{0:%a}", timeNow);
    }
    else if (argument == formatVariant.at(2))
    {
        temp += format("{0:%A}", timeNow);
    }
    else if (argument == formatVariant.at(3))
    {
        temp += format("{0:%b}", timeNow);
    }
    else if (argument == formatVariant.at(4))
    {
        temp += format("{0:%B}", timeNow);
    }
    else if (argument == formatVariant.at(5))
    {
        temp += format("{0:%c}", timeNow);
    }
    else if (argument == formatVariant.at(6))
    {
        temp += format("{0:%C}", timeNow);
    }
    else if (argument == formatVariant.at(7))
    {
        temp += format("{0:%d}", timeNow);
    }
    else if (argument == formatVariant.at(8))
    {
        temp += format("{0:%D}", timeNow);
    }
    else if (argument == formatVariant.at(9))
    {
        temp += format("{0:%e}", timeNow);
    }
    else if (argument == formatVariant.at(10))
    {
        temp += format("{0:%F}", timeNow);
    }
    else if (argument == formatVariant.at(11))
    {
        temp += format("{0:%g}", timeNow);
    }
    else if (argument == formatVariant.at(12))
    {
        temp += format("{0:%G}", timeNow);
    }
    else if (argument == formatVariant.at(13))
    {
        temp += format("{0:%h}", timeNow);
    }
    else if (argument == formatVariant.at(14))
    {
        temp += format("{0:%H}", timeNow);
    }
    else if (argument == formatVariant.at(15))
    {
        temp += format("{0:%I}", timeNow);
    }
    else if (argument == formatVariant.at(16))
    {
        temp += format("{0:%j}", timeNow);
    }
    else if (argument == formatVariant.at(17))
    {
        temp += format(" {0:%H}", timeNow);
    }
    else if (argument == formatVariant.at(18))
    {
        temp += format(" {0:%I}", timeNow);
    }
    else if (argument == formatVariant.at(19))
    {
        temp += format("{0:%m}", timeNow);
    }
    else if (argument == formatVariant.at(20))
    {
        temp += format("{0:%M}", timeNow);
    }
    else if (argument == formatVariant.at(21))
    {
        temp += format("{0:%n}", timeNow);
    }
    else if (argument == formatVariant.at(22))
    {
        temp += format("{0:%S}", timeNow);
    }
    else if (argument == formatVariant.at(23))
    {
        temp += format("{0:%p}", timeNow);
    }
    else if (argument == formatVariant.at(24))
    {
        //P
        //temp += format("{0:%p}", timeNow);
    }
    else if (argument == formatVariant.at(25))
    {
        //q
        if ((format("{0:%m}", timeNow) <= "2") && (format("{0:%m}", timeNow) == "12"))
        {
            temp += "1";
        }
        else if ((format("{0:%m}", timeNow) > "2") && (format("{0:%m}", timeNow) <= "5"))
        {
            temp += "2";
        }
        else if ((format("{0:%m}", timeNow) > "5") && (format("{0:%m}", timeNow) <= "8"))
        {
            temp += "3";
        }
        else
        {
            temp += "4";
        }
    }
    else if (argument == formatVariant.at(26))
    {
        temp += format("{0:%r}", timeNow);
    }
    else if (argument == formatVariant.at(27))
    {
        temp += format("{0:%R}", timeNow);
    }
    else if (argument == formatVariant.at(28))
    {
        //s
    }
    else if (argument == formatVariant.at(29))
    {
        temp += format("{0:%S}", timeNow);
    }
    else if (argument == formatVariant.at(30))
    {
        temp += format("{0:%t}", timeNow);
    }
    else if (argument == formatVariant.at(31))
    {
        temp += format("{0:%T}", timeNow);
    }
    else if (argument == formatVariant.at(32))
    {
        temp += format("{0:%u}", timeNow);
    }
    else if (argument == formatVariant.at(33))
    {
        temp += format("{0:%U}", timeNow);
    }
    else if (argument == formatVariant.at(34))
    {
        temp += format("{0:%V}", timeNow);
    }
    else if (argument == formatVariant.at(35))
    {
        temp += format("{0:%w}", timeNow);
    }
    else if (argument == formatVariant.at(36))
    {
        temp += format("{0:%W}", timeNow);
    }
    else if (argument == formatVariant.at(37))
    {
        temp += format("{0:%d}/{0:%m}/{0:%y}", timeNow);
    }
    else if (argument == formatVariant.at(38))
    {
        temp += format("{0:%X}", timeNow);
    }
    else if (argument == formatVariant.at(39))
    {
        temp += format("{0:%y}", timeNow);
    }
    else if (argument == formatVariant.at(40))
    {
        temp += format("{0:%Y}", timeNow);
    }
    else if (argument == formatVariant.at(41))
    {
        temp += format("{0:%z}", timeNow);
    }
    else if (argument == formatVariant.at(42))
    {
        temp += format("{0:%Oz}", timeNow);
    }
    else if (argument == formatVariant.at(43))
    {
        //::z
        temp += format("{0:%Oz}:00", timeNow);
    }
    else if (argument == formatVariant.at(44))
    {
        //:::z
        //temp += format("{0:%Oz}", timeNow);
    }
    else if (argument == formatVariant.at(45))
    {
        temp += format("{0:%Z}", timeNow);
    }
    else
    {
        temp += argument;
    }

    return temp;
}


void date(string nameCommand, string command, vector <string> regularExpressions)
{
    // Реализация команды date
    // Ключи, которые могут использоваться:
    // -I, -R, --rfc-3339, -u, --help, --version
    vector <string> keys = { "", "-I", "--iso-8601", "-R", "--rfc-email", "--rfc-3339=date", "--rfc-3339=seconds", \
                            "--rfc-3339=ns", "-u", "--utc", "--universal", "--help", "--version", "-Idate", "--iso-8601date", \
                            "-Ihours", "--iso-8601hours", "-Iminutes", "--iso-8601minutes", "-Iseconds", "--iso-8601seconds", \
                            "-Ins", "--iso-8601ns" };

    auto timeNow = chrono::zoned_time{ chrono::current_zone(), chrono::system_clock::now() };
    if ((command == keys.at(1)) || (command == keys.at(2)) || (command == keys.at(5)) || (command == keys.at(13)) || (command == keys.at(14)))
    {
        // Пример даты: 2022-12-24
        cout << format("{0:%F}", timeNow) << endl;
    }
    else if ((command == keys.at(3)) || (command == keys.at(4)))
    {
        // Пример даты: Sat, 24 Dec 2022 11:58:52 +0700
        cout << format("{0:%a, %d %b %Y }{0:%R:%OS %z}", timeNow) << endl;
    }
    else if (command == keys.at(6))
    {
        // Пример даты: 2022-12-24 11:59:22+07:00
        cout << format("{0:%F }{0:%R:%OS%Oz}", timeNow) << endl;
    }
    else if (command == keys.at(7))
    {
        // Пример даты: 2022-12-24 11:59:44.3772763+07:00
        cout << format("{0:%F }{0:%R:%S%Oz}", timeNow) << endl;
    }
    else if ((command == keys.at(8)) || (command == keys.at(9)) || (command == keys.at(10)))
    {
        //  Пример даты: Sat 24 Dec 2022 05:00:50 UTC
        auto timeNow = chrono::system_clock::now();
        cout << format("{0:%a %d %b %Y }{0:%R:%OS %Z}", timeNow) << endl;
    }
    else if (command == keys.at(11))
    {
        string filename = "help.txt";
        readFile(filename);
    }
    else if (command == keys.at(12))
    {
        string filename = "version.txt";
        readFile(filename);
    }
    else if ((command == keys.at(15)) || (command == keys.at(16)))
    {
        // Пример даты: 2022-12-24T11:59:22+07:00
        cout << format("{0:%F}T{0:%H%Oz}", timeNow) << endl;
    }
    else if ((command == keys.at(17)) || (command == keys.at(18)))
    {
        // Пример даты: 2022-12-24T11:59:22+07:00
        cout << format("{0:%F}T{0:%R%Oz}", timeNow) << endl;
    }
    else if ((command == keys.at(19)) || (command == keys.at(20)))
    {
        // Пример даты: 2022-12-24T11:59:22+07:00
        cout << format("{0:%F}T{0:%R:%OS%Oz}", timeNow) << endl;
    }
    else if ((command == keys.at(21)) || (command == keys.at(22)))
    {
        // Пример даты: 2022-12-24T11:59:44.3772763+07:00
        cout << format("{0:%F}T{0:%R:%S%Oz}", timeNow) << endl;
    }
    else if (command == keys.at(0))
    {
        //  Пример даты: Sat 24 Dec 2022 11:56:54 +07:00
        cout << format("{0:%a %d %b %Y }{0:%R:%OS %Oz}", timeNow) << endl;
    }
    else
    {
        //  Регулярные выражения
        vector <string> formatVariant = { "%%", "%a", "%A", "%b", "%B", "%c", "%C", "%d", "%D", "%e", \
                                        "%F", "%g", "%G", "%h", "%H", "%I", "%j", "%k", "%l", "%m", \
                                        "%M", "%n", "%N", "%p", "%P", "%q", "%r", "%R", "%s", "%S", \
                                        "%t", "%T", "%u", "%U", "%V", "%w", "%W", "%x", "%X", "%y", \
                                        "%Y", "%z", "%:z", "%::z", "%:::z", "%Z" };
        string buffer;
        buffer = command.substr(0, 2);
        string temp;
        string argument;

        if (buffer == "+'")
        {
            for (int i = 0; i < regularExpressions.size(); i++)
            {
                for (int j = 0; j < regularExpressions[i].length(); j += 2)
                {
                    buffer = regularExpressions[i].substr(j, 2);
                    for (int k = 0; k < formatVariant.size(); k++)
                    {
                        if (i > 0 or i < regularExpressions.size() - 1)
                        {
                            if (buffer != formatVariant[k])
                            {
                                if (buffer.find("%") != string::npos)
                                {
                                    if (buffer.find("%:") != string::npos)
                                    {
                                        buffer = regularExpressions[i].substr(j, 3);
                                        if (buffer.find("%::") != string::npos)
                                        {
                                            buffer = regularExpressions[i].substr(j, 4);
                                            if (buffer.find("%:::") != string::npos)
                                            {
                                                buffer = regularExpressions[i].substr(j, 5);
                                                if (buffer.find("%:::z") != string::npos)
                                                {
                                                    argument = buffer;
                                                    j += 3;
                                                }
                                            }
                                            else if (buffer.find("%::z") != string::npos)
                                            {
                                                argument = buffer;
                                                j += 2;
                                            }
                                        }
                                        else if (buffer.find("%:z") != string::npos)
                                        {
                                            argument = buffer;
                                            j++;
                                        }
                                    }
                                    if (buffer != "%%")
                                    {
                                        int findPercent = 0;
                                        for (findPercent = buffer.find("%", findPercent++); findPercent != string::npos; findPercent = buffer.find("%", findPercent + 1))
                                        {
                                            if (findPercent == 1)
                                            {
                                                argument = buffer.substr(0, 1);
                                                j--;
                                            }
                                            else
                                            {
                                                argument = buffer;
                                            }
                                            cout << formatingString(temp, argument, formatVariant);
                                        }
                                        break;
                                    }
                                    else
                                    {
                                        argument = "%";
                                        cout << formatingString(temp, argument, formatVariant);
                                        break;
                                    }
                                }
                                else
                                {
                                    if ((buffer != "+'") && (buffer != "'"))
                                    {
                                        argument = buffer;
                                        cout << formatingString(temp, argument, formatVariant);
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
                cout << " ";
            }
        }
        else
            cout << "Неверная команда! Введите другую команду" << endl;
    }
}


int main(int argc, char* argv[])
{
    setlocale(0, "");
    // Реализовать команды date, md5sum
    // Имитируем интерфейс командной строки
    string nameCommand;
    string command;
    vector <string> regularExpressions;
    do
    {
        nameCommand = argv[1];

        if (argc == 3)
        {
            command = argv[2];
            regularExpressions.push_back(argv[2]);
            regularExpressions.push_back("");
        }
        else if (argc > 3)
        {
            command = argv[2];
            for (int i = 2; i < argc; i++)
            {
                regularExpressions.push_back(argv[i]);
            }
        }
        else
            command = "";
        if (nameCommand == "date")
        {
            date(nameCommand, command, regularExpressions);
            break;
        }
        else
        {
            cout << "Нет такой команды! Введите другую команду" << endl;
            break;
        }
    } while (nameCommand != "date");

    return 0;
}
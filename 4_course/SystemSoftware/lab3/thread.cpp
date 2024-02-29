#include <iostream>
#include <thread>
#include <random>
#include <map>
#include <mutex>

using namespace std;


mutex threadLock;

map <unsigned int, bool> free_id  = {
    {1, true},
    {2, true},
    {3, true},
    {4, true},
    {5, true},
    {6, true},
    {7, true},
    {8, true},
    {9, true},
};  //  Карта идентификаторов
    

void secondaryThread(unsigned int &countThread, int id)
{
    //  Функция для второстепенных потоков
    unsigned int randomNumber;
    
    do
    {
        //  Поток выполняется до тех пор, пока не будет сгенерирован 0
        _sleep(1000);

        srand(time(nullptr) + rand() * id);
        randomNumber = rand() % 9;
        if (randomNumber == 0)
        {
            //  Уменьшаем счетчик потоков и завершаем поток
            cout << "thread_" << id << "\tcompleted" << endl;
            threadLock.lock();
            countThread--;
            threadLock.unlock();
        }
        else
        {
            //  Выводим информацию о потоке
            cout << "thread_" << id << "\tnumber:\t" << randomNumber << endl;
        }
    } while (randomNumber != 0);
}


void majorThread(unsigned int countThread)
{
    //  Функция главного потока
    cout << "major thread" << endl;
    int newThreadID;
    int endMap = free_id.size();

    thread* threads[10] = {0};
    while (free_id[endMap] != false)
    {
        //  Проверяем есть ли свободные идентификаторы
        if (countThread < 3)
        {
            //  Создаем новый поток, как только какой-то из вторичных завершился
            threadLock.lock();
            countThread++;
            for (int i = 0; i < free_id.size(); i++)
            {
                if (free_id[i] == true)
                {
                    //  Ищем незанятый идентификатор
                    newThreadID = i;
                    free_id[i] = false;

                    // Добавляем новый поток
                    threads[i] = new thread(secondaryThread, ref(countThread), newThreadID);
                    break;
                }
            }
            threadLock.unlock();
        }
    }
    cout << "major thread completed" << endl;
    return;
}


int main()
{
    unsigned int countThread = 0;

    //  Создаем главный поток
    thread thread(majorThread, countThread);
    thread.join();

    return 0;
}
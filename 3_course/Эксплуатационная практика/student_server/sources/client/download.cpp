#include "download.h"

Download::Download(QObject *parent)
    :QObject(parent)
{
    managerGroup = new QNetworkAccessManager ();
    connect(managerGroup, &QNetworkAccessManager::finished, this, &Download::onResultGroup);

    managerStud = new QNetworkAccessManager ();
    connect(managerStud, &QNetworkAccessManager::finished, this, &Download::onResultStud);

    managerPers = new QNetworkAccessManager ();
    connect(managerPers, &QNetworkAccessManager::finished, this, &Download::onResultPres);
}

void Download::getDataGroup()
{
    QUrl studGroup("http://192.168.0.10/groups"); // Стучимся туда, где расположен файл
    QNetworkRequest requestGroup;
    requestGroup.setUrl(studGroup);
    managerGroup->get(requestGroup);  // Отправляем запрос
}

void Download::getDataStud(QString comboGroup)
{
    if (comboGroup == "Все группы")
    {
        QUrl stud("http://192.168.0.10/groups/all"); // Стучимся туда, где расположен файл
        QNetworkRequest requestStud;
        requestStud.setUrl(stud);
        managerStud->get(requestStud);  // Отправляем запрос
    }
    else
    {
        QUrl stud("http://192.168.0.10/groups/" + comboGroup); // Стучимся туда, где расположен файл
        QNetworkRequest requestStud;
        requestStud.setUrl(stud);
        managerStud->get(requestStud);  // Отправляем запрос
    }

    QUrl studPres("http://192.168.0.10/timerecords"); // Стучимся туда, где расположен файл
    QNetworkRequest requestPres;
    requestPres.setUrl(studPres);
    managerPers->get(requestPres);  // Отправляем запрос
}

void Download::onResultGroup(QNetworkReply *reply)
{
    if (reply->error()) // Проверка наличия ошибок во время выполнения запроса
    {
        qDebug() << "Error";
        qDebug() << reply->errorString();
    }
    else
    {
        QFile *questGroup = new QFile ("/home/group.json"); // Создаем новый файл и копируем туда содержимое полученного файла для дальнейшей обработки
        if(questGroup->open(QFile::WriteOnly))
        {
            questGroup->write(reply->readAll());
            questGroup->close();
        }
        qDebug() << "Download is completed";
        emit onReady();
    }
}

void Download::onResultStud(QNetworkReply *reply)
{
    if (reply->error()) // Проверка наличия ошибок во время выполнения запроса
    {
        qDebug() << "Error";
        qDebug() << reply->errorString();

    }
    else
    {
        QFile *questStud = new QFile ("/home/student.json"); // Создаем новый файл и копируем туда содержимое полученного файла для дальнейшей обработки
        if(questStud->open(QFile::WriteOnly))
        {
            questStud->write(reply->readAll());
            questStud->close();
        }
        qDebug() << "Download is completed";
        emit onReady();
    }
}

void Download::onResultPres(QNetworkReply *reply)
{
    if (reply->error()) // Проверка наличия ошибок во время выполнения запроса
    {
        qDebug() << "Error";
        qDebug() << reply->errorString();

    }
    else
    {
        QFile *questPres = new QFile ("/home/timerecord.json"); // Создаем новый файл и копируем туда содержимое полученного файла для дальнейшей обработки
        if(questPres->open(QFile::WriteOnly))
        {
            questPres->write(reply->readAll());
            questPres->close();
        }
        qDebug() << "Download is completed";
        emit onReady();
    }
}

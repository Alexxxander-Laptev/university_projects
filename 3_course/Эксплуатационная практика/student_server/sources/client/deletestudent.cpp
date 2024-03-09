#include "deletestudent.h"
#include "ui_deletestudent.h"

#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkReply>
#include <QtNetwork/QNetworkRequest>

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

DeleteStudent::DeleteStudent(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::DeleteStudent)
{
    ui->setupUi(this);
    setWindowTitle("Подтверждение удаления");
}

DeleteStudent::~DeleteStudent()
{
    delete ui;
}

void DeleteStudent::on_cancel_clicked()
{
    this->close();
    emit deleteString();
}

void DeleteStudent::readyRequest(QNetworkReply* reply)
{
    if (reply->error() == QNetworkReply::NoError)   // Проверяем, что запрос завершился без ошибок
    {
        qDebug() << "File post";
        reply->deleteLater();
    }
    else
    {
        qDebug() << reply->errorString();
    }
}

void DeleteStudent::studentDelete(QStringList deleteStud)
{
    QJsonObject main;
    QJsonArray student;
    QJsonObject data;
    // Записываем данные студента для операции удаления
    main.insert("action", QJsonValue::fromVariant("remove"));

    int id = deleteStud.at(0).toInt();
    data.insert("fName", QJsonValue::fromVariant(deleteStud.at(1)));
    data.insert("group", QJsonValue::fromVariant(deleteStud.at(4)));
    data.insert("id", QJsonValue::fromVariant(id));
    data.insert("lName", QJsonValue::fromVariant(deleteStud.at(2)));
    data.insert("mName", QJsonValue::fromVariant(deleteStud.at(3)));
    student.push_front(data);
    main.insert("data", student);

    QJsonDocument file(main);

    QString jsonString = file.toJson(QJsonDocument::Indented);
    //Записываем данные в файл
    QFile json;
    json.setFileName("/home/deleteStudent.json");
    json.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream stream( &json );
    stream << jsonString;
    json.close();
}

void DeleteStudent::on_del_clicked()
{
    // Отправка файла с данными студента, которого нужно удалить
    QFile *askDelStud = new QFile ("/home/deleteStudent.json");
    if(askDelStud->open(QFile::ReadOnly))
    {
        QByteArray data = askDelStud->readAll();
        QJsonDocument file = file.fromJson(data);

        QUrl resource("http://192.168.0.10/groups/all");
        QNetworkAccessManager* postDelStud = new QNetworkAccessManager(this);
        connect(postDelStud, SIGNAL(finished(QNetworkReply*)), this, SLOT(readyRequest(QNetworkReply*)));

        QNetworkRequest request(resource);
        request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");

        postDelStud->post(request, data);
    }

    this->close();
    emit deleteString();
}

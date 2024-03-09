#include "alertstudent.h"
#include "ui_alertstudent.h"

#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkReply>
#include <QtNetwork/QNetworkRequest>

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

AlertStudent::AlertStudent(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AlertStudent)
{
    ui->setupUi(this);
    setWindowTitle("Подтверждение изменений");
}

AlertStudent::~AlertStudent()
{
    delete ui;
}

void AlertStudent::on_cancel_clicked()
{
    this->close();
    emit alertString();
}

void AlertStudent::readyRequest(QNetworkReply* reply)
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

void AlertStudent::studentAlert(QStringList alertStud)
{
    QJsonObject main;
    QJsonArray student;
    QJsonObject data;
    // Добавляем в файл измененные данные о студенте
    main.insert("action", QJsonValue::fromVariant("alter"));

    int id = alertStud.at(4).toInt();
    data.insert("id", QJsonValue::fromVariant(id));
    data.insert("lName", QJsonValue::fromVariant(alertStud.at(3)));
    data.insert("fName", QJsonValue::fromVariant(alertStud.at(2)));
    data.insert("mName", QJsonValue::fromVariant(alertStud.at(1)));
    data.insert("group", QJsonValue::fromVariant(alertStud.at(0)));
    student.push_front(data);
    main.insert("data", student);

    QJsonDocument file(main);

    QString jsonString = file.toJson(QJsonDocument::Indented);
    //Записываем данные в файл
    QFile json;
    json.setFileName("/home/alertStudent.json");
    json.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream stream( &json );
    stream << jsonString;
    json.close();
}

void AlertStudent::on_alert_clicked()
{
    // Отправляем данные об изменении информации о студенте
    QFile *askAlertStud = new QFile ("/home/alertStudent.json");
    if(askAlertStud->open(QFile::ReadOnly))
    {
        QByteArray data = askAlertStud->readAll();
        QJsonDocument file = file.fromJson(data);

        QUrl resource("http://192.168.0.10/groups/all");
        QNetworkAccessManager* postAlertStud = new QNetworkAccessManager(this);
        connect(postAlertStud, SIGNAL(finished(QNetworkReply*)), this, SLOT(readyRequest(QNetworkReply*)));

        QNetworkRequest request(resource);
        request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");

        postAlertStud->post(request, data);
    }

    this->close();
    emit alertString();
}

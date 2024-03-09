#include "addstudent.h"
#include "ui_addstudent.h"

#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkReply>
#include <QtNetwork/QNetworkRequest>

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

AddStudent::AddStudent(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AddStudent)
{
    ui->setupUi(this);
}

AddStudent::~AddStudent()
{
    delete ui;
}

void AddStudent::on_cancel_clicked()
{
    this->close();
    emit addString();
}

void AddStudent::readyRequest(QNetworkReply* reply)
{
    if (reply->error() == QNetworkReply::NoError)
    {
        qDebug() << "File post";
        reply->deleteLater();
    }
    else
    {
        qDebug() << reply->errorString();
    }
}

void AddStudent::on_save_clicked()
{
    ui->lName->clear();
    ui->fName->clear();
    ui->mName->clear();
    ui->numGroup->clear();
    lName = ui->lName->text();  // Получаем данные из формы
    fName = ui->fName->text();
    mName = ui->mName->text();
    group = ui->numGroup->text();

    QJsonObject main;
    QJsonArray student;
    QJsonObject data;

    main.insert("action", QJsonValue::fromVariant("add"));

    data.insert("lName", QJsonValue::fromVariant(lName));
    data.insert("fName", QJsonValue::fromVariant(fName));
    data.insert("mName", QJsonValue::fromVariant(mName));
    data.insert("group", QJsonValue::fromVariant(group));
    student.push_back(data);
    main.insert("data", student);

    QJsonDocument file(main);

    QString jsonString = file.toJson(QJsonDocument::Indented);
    //Записываем данные в файл
    QFile json;
    json.setFileName("/home/addStudent.json");
    json.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream stream( &json );
    stream << jsonString;
    json.close();

//    POST-запрос/отправка файла
    QFile *askNewStud = new QFile ("/home/addStudent.json");
    if(askNewStud->open(QFile::ReadOnly))
    {
        QByteArray data = askNewStud->readAll();
        QJsonDocument file = file.fromJson(data);

        QUrl resource("http://192.168.0.10/groups/all");
        QNetworkAccessManager* postNewStud = new QNetworkAccessManager(this);
        connect(postNewStud, SIGNAL(finished(QNetworkReply*)), this, SLOT(readyRequest(QNetworkReply*)));

        QNetworkRequest request(resource);
        request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");

        postNewStud->post(request, data);
    }

    this->close();
    emit addString();
}

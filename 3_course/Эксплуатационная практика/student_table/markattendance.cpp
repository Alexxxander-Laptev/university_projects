#include "markattendance.h"
#include "ui_markattendance.h"
#include "download.h"
#include "checkboxdelegate.h"

#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkReply>
#include <QtNetwork/QNetworkRequest>

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

#include <QCheckBox>
#include <QAbstractItemDelegate>

MarkAttendance::MarkAttendance(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::MarkAttendance)
{
    ui->setupUi(this);

    download = new Download ();
    connect(this, SIGNAL(getGroup(QString)), download, SLOT(getDataStud(QString)));
    connect(ui->select, SIGNAL(clicked()), this, SLOT(numGroup()));  // получаем данные по нажатию на кнопку
    connect(download, &Download::onReady, this, &MarkAttendance::readStud);    // вызываем функцию чтения файла
    connect(ui->save, SIGNAL(clicked()), this, SLOT(postData()));

    tableMark = new QStandardItemModel (ui->tableMark);   // Инициализируем таблицу
}

MarkAttendance::~MarkAttendance()
{
    delete ui;
}

void MarkAttendance::readGroup()
{
    tableMark->clear();
    ui->comboBox->clear();
    ui->comboBox->addItem("Все группы");

    QFile questGroup("/home/admin1/group.json");
//    QFile questGroup("C://Users//Lapte//Documents//group.json");
    if (!questGroup.open(QIODevice::ReadOnly))
        return;

    QByteArray dataG = questGroup.readAll();   // Парсинг файла с номерами групп
    QJsonDocument documentG = documentG.fromJson(dataG);
    QJsonObject root = documentG.object();
    root.value("data");
    QJsonValue groups = root.value("data");
    if(groups.isArray())
    {
        QJsonArray group = groups.toArray();
        for (int i = 0; i < group.count(); i++) {   // Работа с выпадающим списком
            ui->comboBox->addItem(group[i].toString());
        }
    }
}

void MarkAttendance::readStud()
{
    tableMark->clear();
    ui->dateEdit->clear();
    ui->timeEdit->clear();
    CheckBoxDelegate *delegate = new CheckBoxDelegate();

    date = ui->dateEdit->date().toString("yyyy/MM/dd");
    time = ui->timeEdit->time().toString();

    QFile questStud("/home/admin1/student.json");
//    QFile questStud("C://Users//Lapte//Documents//student.json");
    if (!questStud.open(QIODevice::ReadOnly))
        return;
    QByteArray dataS = questStud.readAll();   // Парсинг файла со студентами
    QJsonDocument documentS = documentS.fromJson(dataS);
    QJsonObject root = documentS.object();
    root.value("data");
    QJsonValue students = root.value("data");
    if(students.isArray())
    {
        QJsonArray student = students.toArray();
        markPres = new QCheckBox ();
        QJsonObject main;
        QJsonArray timerec;
        QJsonObject data;

        main.insert("actions", QJsonValue::fromVariant("add"));

        tableMark->setHorizontalHeaderLabels(QStringList() << "id" << "Фамилия" << "Имя" << "Отчество" << "Номер группы" << "Был/Не был");
        for (int i = 0; i < student.count(); i++) {
            QJsonObject personal = student.at(i).toObject();

            QList<QStandardItem *> items;
            items.append(new QStandardItem(QString::number(personal.value("id").toInt())));    // Скрытая колонка
            items.append(new QStandardItem(personal.value("lName").toString()));    // Первая колонка
            items.append(new QStandardItem(personal.value("fName").toString()));    // Вторая колонка
            items.append(new QStandardItem(personal.value("mName").toString()));    // Третья колонка
            items.append(new QStandardItem(personal.value("group").toString()));    // Четвертая колонка
            tableMark->appendRow(items);
            int id = personal.value("id").toInt();
            data.insert("date", QJsonValue::fromVariant(date));
            data.insert("id", QJsonValue::fromVariant(id));
            data.insert("time", QJsonValue::fromVariant(time));
            timerec.push_back(data);
            main.insert("data", timerec);
        }
        ui->tableMark->setItemDelegateForColumn(5, delegate);

        QJsonDocument file(main);

        QString jsonString = file.toJson(QJsonDocument::Indented);
        //Записываем данные в файл
        QFile json;
//        json.setFileName("C://Users//Lapte//Documents//time.json");
        json.setFileName("/home/admin1/time.json");
        json.open(QIODevice::WriteOnly | QIODevice::Text);
        QTextStream stream( &json );
        stream << jsonString;
        json.close();
    }
    ui->tableMark->setModel(tableMark);   // Устанавливаем модель для таблицы
    ui->tableMark->resizeColumnsToContents();
    ui->tableMark->setColumnHidden(0, true);
//    ui->tableMark->horizontalHeader()->setStretchLastSection(true);
    questStud.close();

    QFile presentAbsent("/home/admin1/pres.txt");
    if (!presentAbsent.open(QIODevice::WriteOnly | QIODevice::Text))
        return;
    presentAbsent.close();
}

void MarkAttendance::handleEndOfRequest(QNetworkReply* reply)
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

void MarkAttendance::postData()
{
    QFile timeStud("/home/admin1/time.json");
//    QFile timeStud("C://Users//Lapte//Documents//time.json");
    if (!timeStud.open(QIODevice::ReadOnly))
        return;
    QByteArray dataTimeStud = timeStud.readAll();
    QJsonDocument docTimeStud = docTimeStud.fromJson(dataTimeStud);
    QJsonObject root = docTimeStud.object();
    root.value("data");
    QJsonValue timeStudValue = root.value("data");

    QFile presentAbsent("/home/admin1/pres.txt");
    if (!presentAbsent.open(QIODevice::ReadOnly | QIODevice::Text))
        return;
    while(!presentAbsent.atEnd())
    {
        //читаем строку
        QString str = presentAbsent.readLine();
        if(str == "true\n")
//            pres = true;
            presents.push_back("true");
        else
//            pres = false;
            presents.push_back("false");
    }
    presentAbsent.close();

    if(timeStudValue.isArray())
    {
        QJsonArray timeStudElement = timeStudValue.toArray();
        QJsonObject main;
        QJsonArray timerec;
        QJsonObject data;
        bool pres;

        main.insert("action", QJsonValue::fromVariant("add"));
        for (int i = 0; i < timeStudElement.count(); i++) {
            QJsonObject present = timeStudElement.at(i).toObject();
            QString date = present.value("date").toString();
            int id = present.value("id").toInt();
            QString time = present.value("time").toString();
            if(presents.at(i) == "true")
                pres = true;
            else
                pres = false;

            data.insert("date", QJsonValue::fromVariant(date));
            data.insert("id", QJsonValue::fromVariant(id));
            data.insert("present", QJsonValue::fromVariant(pres));
            data.insert("time", QJsonValue::fromVariant(time));
            timerec.push_back(data);
            main.insert("data", timerec);
        }
        QJsonDocument file(main);

        QString jsonString = file.toJson(QJsonDocument::Indented);
        QFile json;
//        json.setFileName("C://Users//Lapte//Documents//time.json");
        json.setFileName("/home/admin1/time.json");
        json.open(QIODevice::WriteOnly | QIODevice::Text);
        QTextStream stream( &json );
        stream << jsonString;
        json.close();
    }
    timeStud.close();




















    QFile *askStud = new QFile ("/home/admin1/time.json");
//    QFile *askStud = new QFile ("C://Users//Lapte//Documents//time.json");
    if(askStud->open(QFile::ReadOnly))
    {
        QByteArray data = askStud->readAll();
        QJsonDocument file = file.fromJson(data);

        QUrl resource("http://192.168.0.10/timerecords");
        QNetworkAccessManager* postData = new QNetworkAccessManager(this);
        connect(postData, SIGNAL(finished(QNetworkReply*)), this, SLOT(handleEndOfRequest(QNetworkReply*)));

        QNetworkRequest request(resource);
        request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");

        postData->post(request, data);
    }
}

void MarkAttendance::numGroup()
{
    comboGroup = ui->comboBox->currentText();
    emit getGroup(comboGroup);
}

void MarkAttendance::on_back_clicked()  // Открываем главное окно
{
    this->close();
    emit firstWindow();
}

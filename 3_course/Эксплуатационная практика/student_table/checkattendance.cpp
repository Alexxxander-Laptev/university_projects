#include "checkattendance.h"
#include "ui_checkattendance.h"
#include "download.h"

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

CheckAttendance::CheckAttendance(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::CheckAttendance)
{
    ui->setupUi(this);

    download = new Download (); // Инициируем новый объект загрузки
    connect(this, SIGNAL(getGroup(QString)), download, SLOT(getDataStud(QString)));
    connect(ui->select, SIGNAL(clicked()), this, SLOT(numGroup()));  // получаем данные по нажатию на кнопку
    connect(download, &Download::onReady, this, &CheckAttendance::readStud);    // вызываем функцию чтения файла

    tableCheck = new QStandardItemModel (ui->tableCheck);   // Инициализируем таблицу
}

CheckAttendance::~CheckAttendance()
{
    delete ui;
}

void CheckAttendance::readGroup()
{
    ui->comboBox->clear();
    tableCheck->clear();
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

void CheckAttendance::readStud()
{
    tableCheck->clear();
    QFile questStud("/home/admin1/student.json");
//    QFile questStud("C://Users//Lapte//Documents//student.json");
    if (!questStud.open(QIODevice::ReadOnly))
        return;
    QByteArray dataS = questStud.readAll();   // Парсинг файла со студентами
    QJsonDocument documentS = documentS.fromJson(dataS);
    QJsonObject root = documentS.object();
    root.value("data");
    QJsonValue students = root.value("data");

    QFile questPres("/home/admin1/timerecord.json");
//    QFile questPres("C://Users//Lapte//Documents//timerecord.json");
    if (!questPres.open(QIODevice::ReadOnly))
        return;
    QByteArray dataP = questPres.readAll();   // Парсинг файла с номерами групп
    QJsonDocument documentP = documentP.fromJson(dataP);
    QJsonObject root1 = documentP.object();
    root1.value("data");
    QJsonValue timerecords = root1.value("data");

    QString pres;
    if(timerecords.isArray())
    {
        QJsonArray timerecord = timerecords.toArray();
        if(students.isArray())
        {
            QJsonArray student = students.toArray();

            tableCheck->setHorizontalHeaderLabels(QStringList() << "Фамилия" << "Имя" << "Отчество" << "Номер группы" << "Дата занятия" << "Время занятия" << "Был/Не был");
            for (int i = 0; i < student.count(); i++) {
                QJsonObject personal = student.at(i).toObject();
                for (int j = 0; j < timerecord.count(); j++) {
                    QJsonObject present = timerecord.at(j).toObject();
                    if (personal.value("id").toInt() == present.value("id").toInt())
                    {
                        if(present.value("present").toBool() == true)
                            pres = "Присутствовал";
                        else
                            pres = "Отсутствовал";
                        QList<QStandardItem *> items;
                        items.append(new QStandardItem(personal.value("lName").toString()));    // Первая колонка
                        items.append(new QStandardItem(personal.value("fName").toString()));    // Вторая колонка
                        items.append(new QStandardItem(personal.value("mName").toString()));    // Третья колонка
                        items.append(new QStandardItem(personal.value("group").toString()));    // Четвертая колонка
                        items.append(new QStandardItem(present.value("date").toString()));    // Первая колонка
                        items.append(new QStandardItem(present.value("time").toString()));    // Вторая колонка
                        items.append(new QStandardItem(pres));    // Третья колонка
                        tableCheck->appendRow(items);
                    }
                }
            }
        }
        ui->tableCheck->resizeColumnsToContents();
        ui->tableCheck->setModel(tableCheck);   // Устанавливаем модель для таблицы
    }
}

void CheckAttendance::numGroup()
{
    comboGroup = ui->comboBox->currentText();
    emit getGroup(comboGroup);
}

void CheckAttendance::on_back_clicked()
{
    this->close();
    emit firstWindow();
}

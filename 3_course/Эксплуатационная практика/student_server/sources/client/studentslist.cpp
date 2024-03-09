#include "studentslist.h"
#include "ui_studentslist.h"
#include "download.h"
#include "addstudent.h"
#include "deletestudent.h"

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

StudentsList::StudentsList(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::StudentsList)
{
    ui->setupUi(this);

    add = new AddStudent ();
    connect(add, &AddStudent::addString, this, &AddStudent::show);

    alert = new AlertStudent ();
    connect(this, SIGNAL(postAlertStud(QStringList)), alert, SLOT(studentAlert(QStringList)));
    connect(alert, &AlertStudent::alertString, this, &AlertStudent::show);

    confirm = new DeleteStudent ();
    connect(this, SIGNAL(postDelStud(QStringList)), confirm, SLOT(studentDelete(QStringList)));
    connect(confirm, &DeleteStudent::deleteString, this, &DeleteStudent::show);

    download = new Download (); // Инициируем новый объект загрузки
    connect(this, SIGNAL(getGroup(QString)), download, SLOT(getDataStud(QString)));
    connect(ui->select, SIGNAL(clicked()), this, SLOT(numGroup()));  // получаем данные по нажатию на кнопку
    connect(download, &Download::onReady, this, &StudentsList::readStud);    // вызываем функцию чтения файла

    tableStud = new QStandardItemModel (ui->tableStud);   // Инициализируем таблицу
}

StudentsList::~StudentsList()
{
    delete ui;
}

void StudentsList::readGroup()
{
    tableStud->clear();
    ui->comboBox->clear();
    ui->comboBox->addItem("Все группы");

    QFile questGroup("/home/group.json");
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

void StudentsList::readStud()
{
    tableStud->clear();
    QFile questStud("/home/student.json");
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

        tableStud->setHorizontalHeaderLabels(QStringList() << "id" << "Фамилия" << "Имя" << "Отчество" << "Номер группы");
        for (int i = 0; i < student.count(); i++) {
            QJsonObject personal = student.at(i).toObject();

            QList<QStandardItem *> items;
            items.append(new QStandardItem(QString::number(personal.value("id").toInt())));    // Скрытая колонка
            items.append(new QStandardItem(personal.value("lName").toString()));    // Вторая колонка
            items.append(new QStandardItem(personal.value("fName").toString()));    // Первая колонка
            items.append(new QStandardItem(personal.value("mName").toString()));    // Третья колонка
            items.append(new QStandardItem(personal.value("group").toString()));    // Четвертая колонка
            tableStud->appendRow(items);
        }
    }
    ui->tableStud->resizeColumnsToContents();
    ui->tableStud->setModel(tableStud);   // Устанавливаем модель для таблицы
    ui->tableStud->setColumnHidden(0, true);
}

void StudentsList::numGroup()
{
    comboGroup = ui->comboBox->currentText();
    emit getGroup(comboGroup);
}

void StudentsList::on_back_clicked()
{
    this->close();
    emit firstWindow();
}

void StudentsList::on_add_clicked()
{
    add->show();
}

void StudentsList::on_del_clicked()
{
    // Получаем данные из выделенной строки, которые будут удалены
    QString delStud;
    for (int i = 0; i < 5; i++) {
        delStud = tableStud->data(tableStud->index(ui->tableStud->currentIndex().row(), i)).toString();
        deleteStud.push_back(delStud);
    }
    emit postDelStud(deleteStud);
    confirm->show();
}

void StudentsList::on_alert_clicked()
{
    // Ролучаем измененные данные из текущей строки
    QString alStud;
    for (int i = 0; i < 5; i++) {
        alStud = tableStud->data(tableStud->index(ui->tableStud->currentIndex().row(), i)).toString();
        alertStud.push_front(alStud);
    }
    emit postAlertStud(alertStud);
    alert->show();
}

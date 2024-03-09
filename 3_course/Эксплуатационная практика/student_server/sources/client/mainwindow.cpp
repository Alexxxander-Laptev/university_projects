#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "checkattendance.h"
#include "markattendance.h"
#include "studentslist.h"
#include "download.h"

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    mark = new MarkAttendance ();   // Инициируем окно отметки посещаемости
    connect(mark, &MarkAttendance::firstWindow, this, &MarkAttendance::show);   // Подключаемся к слоту открытия главного окна

    check = new CheckAttendance (); // Инициируем окно просмотра посещаемости
    connect(check, &CheckAttendance::firstWindow, this, &CheckAttendance::show);

    list = new StudentsList (); // Инициируем окно просмотра посещаемости
    connect(list, &StudentsList::firstWindow, this, &StudentsList::show);

    download = new Download (); // Инициируем новый объект загрузки
    connect(ui->check, SIGNAL(clicked()), download, SLOT(getDataGroup()));  // получаем данные по нажатию на кнопку
    connect(ui->mark, SIGNAL(clicked()), download, SLOT(getDataGroup()));
    connect(ui->list, SIGNAL(clicked()), download, SLOT(getDataGroup()));
}

MainWindow::~MainWindow()
{
    delete ui;
    // Удаляем все созданные в процессе работы программы файлы
    QFile *addStud = new QFile ("/home/addStudent.json");
    addStud->remove();

    QFile *alterStud = new QFile ("/home/alertStudent.json");
    alterStud->remove();

    QFile questGroup("/home/group.json");
    questGroup.remove();

    QFile questStud("/home/student.json");
    questStud.remove();

    QFile questPres("/home/timerecord.json");
    questPres.remove();

    QFile *delStud = new QFile ("/home/deleteStudent.json");
    delStud->remove();

    QFile timeStud("/home/time.json");
    timeStud.remove();

    QFile presentAbsent("/home/pres.txt");
    presentAbsent.remove();
}

void MainWindow::on_check_clicked()  // Открываем окно просмотра посещаемости
{
    check->show();
    this->close();
    connect(download, &Download::onReady, check, &CheckAttendance::readGroup);
}

void MainWindow::on_mark_clicked()  // Открываем окно отметки посещаемости
{
    mark->show();
    this->close();
    connect(download, &Download::onReady, mark, &MarkAttendance::readGroup);
}

void MainWindow::on_list_clicked()  // Открываем окно со списком студентов
{
    list->show();
    this->close();
    connect(download, &Download::onReady, list, &StudentsList::readGroup);
}


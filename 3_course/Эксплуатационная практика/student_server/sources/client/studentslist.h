#ifndef STUDENTSLIST_H
#define STUDENTSLIST_H

#include <QWidget>
#include <QStandardItem>
#include <QStandardItemModel>

#include "download.h"
#include "addstudent.h"
#include "deletestudent.h"
#include "alertstudent.h"

namespace Ui {
class StudentsList;
}

class StudentsList : public QWidget
{
    Q_OBJECT

signals:
    void firstWindow();
    void getGroup(QString comboGroup);
    void postDelStud(QStringList deleteStud);
    void postAlertStud(QStringList alertStud);

public:
    explicit StudentsList(QWidget *parent = nullptr);
    ~StudentsList();
    QString comboGroup;
    QStringList deleteStud;
    QStringList alertStud;

public slots:
    void readGroup();
    void readStud();
    void numGroup();

private slots:
    void on_back_clicked();
    void on_add_clicked();
    void on_del_clicked();

    void on_alert_clicked();

private:
    Ui::StudentsList *ui;
    Download *download;
    AddStudent *add;
    DeleteStudent *confirm;
    QStandardItemModel *tableStud;
    AlertStudent *alert;
};

#endif // STUDENTSLIST_H

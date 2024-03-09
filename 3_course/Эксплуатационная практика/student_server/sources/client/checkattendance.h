#ifndef CHECKATTENDANCE_H
#define CHECKATTENDANCE_H

#include <QWidget>
#include <QStandardItem>
#include <QStandardItemModel>

#include "download.h"

namespace Ui {
class CheckAttendance;
}

class CheckAttendance : public QWidget
{
    Q_OBJECT

signals:
    void firstWindow();
    void getGroup(QString comboGroup);

public:
    explicit CheckAttendance(QWidget *parent = nullptr);
    ~CheckAttendance();
    QString comboGroup;

public slots:
    void readGroup();
    void readStud();
    void numGroup();

private slots:
    void on_back_clicked();

private:
    Ui::CheckAttendance *ui;
    Download *download;
    QStandardItemModel *tableCheck;
};

#endif // CHECKATTENDANCE_H

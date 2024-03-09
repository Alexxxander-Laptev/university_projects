#ifndef MARKATTENDANCE_H
#define MARKATTENDANCE_H

#include <QWidget>
#include <QStandardItem>
#include <QStandardItemModel>
#include <QCheckBox>
#include <QStyledItemDelegate>

#include "download.h"
#include "checkboxdelegate.h"

namespace Ui {
class MarkAttendance;
}

class MarkAttendance : public QWidget
{
    Q_OBJECT

signals:
    void firstWindow();
    void getGroup(QString comboGroup);

public:
    explicit MarkAttendance(QWidget *parent = nullptr);
    ~MarkAttendance();
    QString comboGroup;
    QString date;
    QString time;
    QStringList presents;

public slots:
    void readGroup();
    void readStud();
    void postData();
    void handleEndOfRequest(QNetworkReply* reply);
    void numGroup();

private slots:
    void on_back_clicked();

private:
    Ui::MarkAttendance *ui;
    Download *download;
    QStandardItemModel *tableMark;
    QCheckBox *markPres;
    CheckBoxDelegate *cbd;
};

#endif // MARKATTENDANCE_H

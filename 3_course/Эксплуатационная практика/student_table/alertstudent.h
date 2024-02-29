#ifndef ALERTSTUDENT_H
#define ALERTSTUDENT_H

#include <QWidget>

#include "download.h"

namespace Ui {
class AlertStudent;
}

class AlertStudent : public QWidget
{
    Q_OBJECT

signals:
    void alertString();

public:
    explicit AlertStudent(QWidget *parent = nullptr);
    ~AlertStudent();
    QStringList alertStud;

public slots:
    void readyRequest(QNetworkReply*);
    void studentAlert(QStringList alertStud);

private slots:
    void on_cancel_clicked();
    void on_alert_clicked();

private:
    Ui::AlertStudent *ui;
};

#endif // ALERTSTUDENT_H

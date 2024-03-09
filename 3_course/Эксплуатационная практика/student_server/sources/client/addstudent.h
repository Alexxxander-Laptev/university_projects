#ifndef ADDSTUDENT_H
#define ADDSTUDENT_H

#include <QWidget>

#include "download.h"

namespace Ui {
class AddStudent;
}

class AddStudent : public QWidget
{
    Q_OBJECT

signals:
    void addString();

public:
    explicit AddStudent(QWidget *parent = nullptr);
    ~AddStudent();
    QString lName;
    QString fName;
    QString mName;
    QString group;

public slots:
    void readyRequest(QNetworkReply*);

private slots:
    void on_cancel_clicked();
    void on_save_clicked();

private:
    Ui::AddStudent *ui;
};

#endif // ADDSTUDENT_H

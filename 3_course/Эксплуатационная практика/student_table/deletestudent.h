#ifndef DELETESTUDENT_H
#define DELETESTUDENT_H

#include <QWidget>

#include "download.h"

namespace Ui {
class DeleteStudent;
}

class DeleteStudent : public QWidget
{
    Q_OBJECT

signals:
    void deleteString();

public:
    explicit DeleteStudent(QWidget *parent = nullptr);
    ~DeleteStudent();
    QStringList deleteStud;

public slots:
    void readyRequest(QNetworkReply*);
    void studentDelete(QStringList deleteStud);

private slots:
    void on_cancel_clicked();
    void on_del_clicked();

private:
    Ui::DeleteStudent *ui;
};

#endif // DELETESTUDENT_H

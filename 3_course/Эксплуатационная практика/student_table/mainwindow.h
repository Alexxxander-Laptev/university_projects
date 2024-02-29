#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "checkattendance.h"
#include "markattendance.h"
#include "studentslist.h"
#include "download.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_check_clicked();
    void on_mark_clicked();
    void on_list_clicked();

private:
    Ui::MainWindow *ui;
    CheckAttendance *check;
    MarkAttendance *mark;
    StudentsList *list;
    Download *download;
};
#endif // MAINWINDOW_H

#ifndef DOWNLOAD_H
#define DOWNLOAD_H

#include <QObject>
#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkReply>
#include <QtNetwork/QNetworkRequest>
#include <QUrl>
#include <QFile>
#include <QDebug>

class Download : public QObject
{
    Q_OBJECT
public:
    explicit Download(QObject *parent = 0);
    QString comboGroup;

signals:
    void onReady();

public slots:
    void getDataGroup();
    void getDataStud(QString comboGroup);
    void onResultGroup(QNetworkReply *reply);
    void onResultStud(QNetworkReply *reply);
    void onResultPres(QNetworkReply *reply);

private:
    QNetworkAccessManager *managerGroup;
    QNetworkAccessManager *managerStud;
    QNetworkAccessManager *managerPers;
};

#endif // DOWNLOAD_H

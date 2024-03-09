#include "checkboxdelegate.h"

#include <QCheckBox>
#include <QApplication>
#include <QDebug>
#include <QFile>

#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>

CheckBoxDelegate::CheckBoxDelegate(QObject *parent)
    :QStyledItemDelegate (parent)
{

}

QWidget *CheckBoxDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(option)
    Q_UNUSED(index)

    //Cоздаем checkbox editor
    QCheckBox *editor = new QCheckBox(parent);
    return editor;
}

void CheckBoxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    //Установливаем выбрано/не выбрано
    QCheckBox *cb = qobject_cast<QCheckBox *>(editor);
    cb->setChecked(index.data().toBool());
}

void CheckBoxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    //Записываем данные в модель
    QCheckBox *cb = static_cast<QCheckBox *>(editor);
    int value = (cb->checkState()==Qt::Checked)? 1 : 0;
    model->setData(index, value, Qt::EditRole);
    QString text;
    if(value == 1)
        text = "true";
    else
        text = "false";

    QFile presentAbsent("/home/pres.txt");
    if (!presentAbsent.open(QIODevice::Append | QIODevice::Text))
        return;
    QTextStream writeStream(&presentAbsent);
    writeStream << text << "\n";
    presentAbsent.close();
}

void CheckBoxDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(index);
    QStyleOptionButton checkboxstyle;
    QRect checkbox_rect = QApplication::style()->subElementRect(QStyle::SE_CheckBoxIndicator, &checkboxstyle);

    //Центрирование
    checkboxstyle.rect = option.rect;
    checkboxstyle.rect.setLeft(option.rect.x() + option.rect.width()/2 - checkbox_rect.width()/2);

    editor->setGeometry(checkboxstyle.rect);
}

void CheckBoxDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    //Получаем данные
    bool data = index.model()->data(index, Qt::DisplayRole).toBool();

    //Создаем стиль CheckBox
    QStyleOptionButton checkboxstyle;
    QRect checkbox_rect = QApplication::style()->subElementRect(QStyle::SE_CheckBoxIndicator, &checkboxstyle);

    //Центрирование
    checkboxstyle.rect = option.rect;
    checkboxstyle.rect.setLeft(option.rect.x() + option.rect.width()/2 - checkbox_rect.width()/2);
    //Выбрано или не выбрано
    if(data)
        checkboxstyle.state = QStyle::State_On|QStyle::State_Enabled;
    else
        checkboxstyle.state = QStyle::State_Off|QStyle::State_Enabled;

    //Отображаем
    QApplication::style()->drawControl(QStyle::CE_CheckBox, &checkboxstyle, painter);
}

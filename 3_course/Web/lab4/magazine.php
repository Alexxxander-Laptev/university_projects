<!-- Вариант №8:

1) Создать базу данных с таблицами: студенты (id, имя, фамилия, группа), предметы (id, название),
таблица посещаемости (id предмета, id студента, дата занятия, отметка о посещении/отсутствии),
2) Сделать страницу для отметки посещения занятия (предмет брать из списка select, дату вводить в текстовое поле в любом формате на выбор):
список группы, чекбоксы "был/не был" для каждого студента, кнопка сохранения результатов
3) Сделать страницу просмотра посещаемости: выбор предмета, группы, после выбора: вывод результатов в виде таблицы:
в колонках - даты занятий, в строках - ФИО, группа, отметка о посещении.
4) Добавить на страницу посещаемости возможность сортировки списка по фамилии и посещаемости. Выбранный способ сортировки запоминать в cookies. -->

<html>
    <head>
        <title>Тестируем PHP</title>
        <meta charset="utf-8">
        <link href="stylesheet.css" rel="stylesheet">
        <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
        <script src="test.js"></script>
    </head>
    <body>
        <h1>Просмотр посещаемости</h1>
        <form method="post" id="ajax_form">
            Выберите предмет: <select name="subject">
                <option name="sel" value="1">математика</option>
                <option name="sel" value="2">физика</option>
                <option name="sel" value="3">веб-технологии</option>
            </select> 
            Номер группы: <select name="group">
                <option name="gr" value="123">123</option>
                <option name="gr" value="321">321</option>
            </select> 
            <input type="button" id="btn" value="Применить"/>
        </form>
        <div style='display:flex;flex-direction:columns;gap: 20px;'>
        <h4 onclick="sorttest(1)">Cортировка по фамилии</h4><h4 onclick="sorttest(2)">Сортировка по посещаемости</h4>
        </div>
        <div id="result_form" style='display:flex;flex-direction:row;'></div>
    </body>
<html>
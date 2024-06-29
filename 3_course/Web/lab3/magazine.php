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
    </head>
    <body>
        <h1>Просмотр посещаемости</h1>
        <form method="post" action="magazine.php">
            Выберите предмет: <select name="subject">
                <option name="sel" value="1">математика</option>
                <option name="sel" value="2">физика</option>
                <option name="sel" value="3">веб-технологии</option>
            </select> 
            Номер группы: <select name="group">
                <option name="gr" value="123">123</option>
                <option name="gr" value="321">321</option>
            </select>
            Сортировать: <select name="sort_sel">
                <option name="sort" value="1">по фамилии</option>
                <option name="sort" value="2">по успеваемости</option>
            </select>
            <input type="submit" value="Применить" />
        </form>
        <table id="tab">
        <div  style="display: flex;flex-direction:row;">
            <?php
                $data = [];
                $data1 = [];
                $link = mysqli_connect("", "lab3", "123", "lab3");   
                $query = "SELECT DISTINCT(date_subject) FROM `STUD`, `VISIT` WHERE visit.SUBJECT_ID_SUBJECT=".$_POST['subject']." AND STUD.GROUP_VISIT=".$_POST['group'];
                $result = mysqli_query($link, $query);
                echo "<div style='display:flex;flex-direction:column;'>";
                while($date = mysqli_fetch_array($result))
                {
                    echo "<h3>".$date['date_subject']."</h3>";
                    // echo "<dl>";
                    $query = "SELECT DISTINCT(`id_stud`), `surename`, `name`, `group_visit`, `present_absent` FROM `STUD` INNER JOIN `visit` ON `stud`.`id_stud` = `visit`.`stud_id_stud` WHERE STUD.GROUP_VISIT=".$_POST['group']." and visit.date_subject='".$date['date_subject']."' AND visit.subject_id_subject = ".$_POST['subject'];
                    $result2 = mysqli_query($link, $query);
                    while($row = mysqli_fetch_array($result2))
                    {
                        // echo "<dt id='tabtd'>".$row['surename']."\t".$row['name']."\t".$row['group_visit']."\t".$row['present_absent']."</dt>\n";
                        $data1 = ['surename' => $row['surename'], 'name' => $row['name'], 'gr_vis' => $row['group_visit'], 'pres' => $row['present_absent']];
                        array_push($data, $data1);
                        // echo "<dt id='tabtd'>".join(' ', $data1)."</dt>\n";
                    }
                    // echo "</dl>";
                    if ($_POST['sort_sel'] == 1)
                    { 
                        usort($data, function ($a, $b)
                        {
                            if($a['surename'] == $b['surename'])
                                return 0;
                        
                            if($a['surename'] < $b['surename'])
                                return -1;
                            else
                                return 1;
                        });
                    }
                    else
                    {
                        usort($data, function ($a, $b)
                        {
                            if($a['pres'] == $b['pres'])
                                return 0;
                        
                            if($a['pres'] < $b['pres'])
                                return -1;
                            else
                                return 1;
                        });
                    }
                    foreach($data as $people)
                    {
                        echo "<tr>";
                        foreach($people as $user)
                        {
                            echo "<td id='tabtd'>$user</td>";
                        }
                        echo "<tr>";
                    }
                }
                echo "</div>";       
                mysqli_close($link);
            ?>
        </div>
        </table>
    </body>
<html>
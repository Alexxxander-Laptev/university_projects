<html>
    <head>
        <title>Тестируем PHP</title>
        <meta charset="utf-8">
        <link href="stylesheet.css" rel="stylesheet">
    </head>
    <body>
        <h1>Отметка посещаемости</h1>
        <form method="post" action="visit.php">
            Выберите предмет: <select name="subject">
                <option name="sel" value="1">математика</option>
                <option name="sel" value="2">физика</option>
                <option name="sel" value="3">веб-технологии</option>
            </select> 
            <input type="date" name="selected_date">
            <table id="tab">
                <caption>Список студентов:</caption>
                <tr>
                    <th class='tabtd1'>Фамилия</th>
                    <th class='tabtd1'>Имя</th>
                    <th class='tabtd1'>Номер Группы</th>
                    <th class='tabtd1'>Посещаемость</th>
                </tr>
                <?php
                    $link = mysqli_connect("", "lab3", "123", "lab3");
                    $i = 0;
                    $query = "SELECT * FROM `STUD`";
                    $result = mysqli_query($link, $query);
                    while($row = mysqli_fetch_array($result))
                    {
                        echo "<tr>
                        <td id='tabtd'><input type='text' name='student[".$i."][id_stud]' value='".$row['id_stud']."' hidden>".$row['surename']."</td>
                        <td id='tabtd'>".$row['name']."</td>
                        <td id='tabtd'>".$row['group_visit']."</td>
                        <td id='tabtd'><input type='checkbox' name='student[".$i."][ch]' value='1'></td> 
                        </tr>";
                        $i++;
                    }
                    $students_visit = $_POST['student'];
                    $subject = $_POST['subject'];
                    $date = $_POST['selected_date'];
                    foreach ($students_visit as $stud) 
                    {
                        if(isset($stud['ch'])){
                            $write = "INSERT INTO `VISIT` (`STUD_ID_STUD`, `SUBJECT_ID_SUBJECT`, `DATE_SUBJECT`, `PRESENT_ABSENT`) VALUES ('".$stud['id_stud']."',".$subject.", '".$date."', 1)";
                        }else{
                            $write = "INSERT INTO `VISIT` (`STUD_ID_STUD`, `SUBJECT_ID_SUBJECT`, `DATE_SUBJECT`, `PRESENT_ABSENT`) VALUES ('".$stud['id_stud']."',".$subject.", '".$date."', 0)";
                        }
                        $wr_res = mysqli_query($link, $write);
                    }
                    mysqli_close($link);
                ?>
            </table>
            <button type="submit">Save</button>
        </form>
    </body>
</html>
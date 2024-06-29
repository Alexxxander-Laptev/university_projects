<html>
    <head>
        <title>Тестируем PHP</title>
        <meta charset="utf-8">
        <link href="stylesheet.css" rel="stylesheet">
    </head>
    <body>
        <form action="style_select.php" method="post">
            <select name="select">
                <option>Выберите стиль оформления</option>
                <?php
                $sch = array(0, 1, 2, 3, 4);

                echo '<option name="sel" value="'.$sch[0].'">aqua_1</option>';
                echo '<option name="sel1" value="'.$sch[1].'">cadetblue_1</option>';
                echo '<option name="sel2" value="'.$sch[2].'">burlywood_1</option>';
                echo '<option name="sel3" value="'.$sch[3].'">aqua_2</option>';
                echo '<option name="sel4" value="'.$sch[4].'">cadetblue_2</option>';
                ?>
            </select>
            <INPUT TYPE="submit" value="Применить" />
        </form>
    </body>
</html>
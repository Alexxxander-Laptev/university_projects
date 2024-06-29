<html>
    <head>
        <title>Тестируем PHP</title>
        <meta charset="utf-8">
        <link href="stylesheet.css" rel="stylesheet">
    </head>
    <body>
        <?php
        if ($_POST['select'] == 0)
        {
            include 'theme1.php';
        }

        if ($_POST['select'] == 1)
        {
            include 'theme2.php';
        }

        if ($_POST['select'] == 2)
        {
            include 'theme3.php';
        }

        if ($_POST['select'] == 3)
        {
            include 'theme4.php';
        }

        if ($_POST['select'] == 4)
        {
            include 'theme5.php';
        }
        ?>
    </body>
</html>
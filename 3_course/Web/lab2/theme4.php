<html>
    <head>
        <title>Тестируем PHP</title>
        <meta charset="utf-8">
        <link href="stylesheet.css" rel="stylesheet">
    </head>
    <body>
        <table id="tab">
        <?php
        class ArTab4
        {
            var $data;
            var $head;

            function Tab4()
            {
                $head = array("Name", "Surename", "Patronomyc", "Age", "Phone");
                echo "<tr>";
                echo "<th id='tabtd4'>$head[0] <form action = 'theme4.php' method='POST' ><input name = 'sort' type='submit' value='sort max'/><input name = 'sort5' type='submit' value='sort min'/></form></th>";
                echo "<th id='tabtd4'>$head[1] <form action = 'theme4.php' method='POST' ><input name = 'sort1' type='submit' value='sort max'/><input name = 'sort6' type='submit' value='sort min'/></form></th>";
                echo "<th id='tabtd4'>$head[2] <form action = 'theme4.php' method='POST' ><input name = 'sort2' type='submit' value='sort max'/><input name = 'sort7' type='submit' value='sort min'/></form></th>";
                echo "<th id='tabtd4'>$head[3] <form action = 'theme4.php' method='POST' ><input name = 'sort3' type='submit' value='sort max'/><input name = 'sort8' type='submit' value='sort min'/></form></th>";
                echo "<th id='tabtd4'>$head[4] <form action = 'theme4.php' method='POST' ><input name = 'sort4' type='submit' value='sort max'/><input name = 'sort9' type='submit' value='sort min'/></form></th>";
                echo "<tr>";

                $data = [['name' => "Александр", 'sur' => "Иванов", 'pat' => "Вячеславович", 'date' => 25, 'phone' => "88889991234"],
                ['name' => "Иван", 'sur' => "Петров", 'pat' => "Владимирович", 'date' => 34, 'phone' => "89998881234"],
                ['name' => "Владислав", 'sur' => "Сидоров", 'pat' => "Иванович", 'date' => 41, 'phone' => "88889993412"]];
                
                if (isset($_POST['sort']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['name'] == $b['name'])
                            return 0;
                    
                        if($a['name'] > $b['name'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort1']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['sur'] == $b['sur'])
                            return 0;
                    
                        if($a['sur'] > $b['sur'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort2']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['pat'] == $b['pat'])
                            return 0;
                    
                        if($a['pat'] > $b['pat'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort3']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['date'] == $b['date'])
                            return 0;
                    
                        if($a['date'] > $b['date'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort4']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['phone'] == $b['phone'])
                            return 0;
                    
                        if($a['phone'] > $b['phone'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort5']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['name'] == $b['name'])
                            return 0;
                    
                        if($a['name'] < $b['name'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort6']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['sur'] == $b['sur'])
                            return 0;
                    
                        if($a['sur'] < $b['sur'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort7']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['pat'] == $b['pat'])
                            return 0;
                    
                        if($a['pat'] < $b['pat'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort8']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['date'] == $b['date'])
                            return 0;
                    
                        if($a['date'] < $b['date'])
                            return -1;
                        else
                            return 1;
                    });
                }

                if (isset($_POST['sort9']))
                {
                    usort($data, function ($a, $b)
                    {
                        if($a['phone'] == $b['phone'])
                            return 0;
                    
                        if($a['phone'] < $b['phone'])
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
        }
        $object4 = new ArTab4;
        echo $object4 -> Tab4();
        ?>
        </table>
    </body>
</html>
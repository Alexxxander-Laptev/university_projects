<?php
// ini_set('error_reporting', E_ALL);
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
error_reporting(E_ERROR | E_PARSE);
$data_end = [];
$params = array(
    'expires' => time()+60*60*24*1,
    'path' => ini_get('session.cookie_path'),
    'domain' => $_SERVER['HTTP_HOST'],
    'secure' => 0,
    'httponly' => 0,
    'SameSite' => 'None'
);
$sort_query = '';
if (isset($_POST["subject"]) && isset($_POST["group"]) ) {
    $link = mysqli_connect("", "lab3", "123", "lab3");   
    $query = "SELECT DISTINCT(date_subject) FROM `STUD`, `VISIT` WHERE visit.SUBJECT_ID_SUBJECT=".$_POST['subject']." AND STUD.GROUP_VISIT=".$_POST['group'];
    $result = mysqli_query($link, $query);
    // echo "<div style='display:flex;flex-direction:column;'>";
    while($date = mysqli_fetch_array($result))
    {
        // echo "<h3>".$date['date_subject']."</h3>";
        // echo "<dl>";
        $data1 = [];
        $data['date'] = $date;
        $data['data'] = [];
        
        if($_COOKIE['sort'] == null){
            setcookie('sort','',$params);
        } else {
            $sort_query = $_COOKIE['sort'];
        }
        // echo $sort_query;
        $query = "SELECT DISTINCT(`id_stud`), `surename`, `name`, `group_visit`, `present_absent` FROM `STUD` INNER JOIN `visit` ON `stud`.`id_stud` = `visit`.`stud_id_stud` WHERE STUD.GROUP_VISIT=".$_POST['group']." and visit.date_subject='".$date['date_subject']."' AND visit.subject_id_subject = ".$_POST['subject']." ".$sort_query;
        $result2 = mysqli_query($link, $query);
        while($row = mysqli_fetch_array($result2))
        {
            $temp = ['surename' => $row['surename'], 'name' => $row['name'], 'gr_vis' => $row['group_visit'], 'pres' => $row['present_absent']];
            array_push($data1, $temp);
        }
        $data['data']= $data1;
        array_push($data_end, $data);
        // foreach($data as $people)
        // {
        //     echo "<tr>";
        //     foreach($people as $user)
        //     {
        //         echo "<td id='tabtd'>$user</td>";
        //     }
        //     echo "<tr>";
        // }
        // echo "</dl>";
    }

    // echo "</div>";
    mysqli_close($link);
    echo json_encode($data_end);
}

?>
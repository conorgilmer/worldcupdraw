<?php
   $group=$_GET["q"];

 $file = "seedings.csv";
 $c=0;

  echo "{ \"cols\": [ {\"id\":\"\",\"label\":\"Country\",\"pattern\":\"\",\"type\":\"string\"}, {\"id\":\"\",\"label\":\"Position\",\"pattern\":\"\",\"type\":\"number\"} , {\"id\":\"\",\"role\":\"style\",\"type\":\"string\"} ], \"rows\": [ ";
   
$data=fopen($file,'r');
while($row=fgets($data)){
    //$row is your line as a string
    if($c!=0){
    //do something with it
    $lst = explode(",", $row);
        if ($lst[5]== $group){ 
      echo "{\"c\":[{\"v\":\"" . $lst[2] . "\",\"f\":null},{\"v\":" . $lst[3] . ",\"f\":null},{\"v\":\"#0000FF\",\"f\":null} ]},";
    } else {
//      echo "{\"c\":[{\"v\":\"" . 'others' . "\",\"f\":null},{\"v\":" . $row['others'] . ",\"f\":null}]}, ";
    }
  }
  $c++;
}
  echo " ] }";
?>

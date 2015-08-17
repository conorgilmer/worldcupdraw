<?php
   $group=$_GET["q"];
   $colours = array("#0000FF","#FF00AA","#00FF00","#3300AA","#FF0000","#333222","#342000","#1110FF","#222222");
 $file = "seedings.csv";
 $c=0;
 $col=0;
  echo "{ \"cols\": [ {\"id\":\"\",\"label\":\"Country\",\"pattern\":\"\",\"type\":\"string\"}, {\"id\":\"\",\"label\":\"Position\",\"pattern\":\"\",\"type\":\"number\"} , {\"id\":\"\",\"role\":\"style\",\"type\":\"string\"} ], \"rows\": [ ";
   
$data=fopen($file,'r');
while($row=fgets($data)){
    //$row is your line as a string
    if($c!=0){
    //do something with it
    $lst = explode(",", $row);
        if ($lst[5]== $group){
	$pos = 4.5 - ($lst[0] - (9 * $col)); 
      echo "{\"c\":[{\"v\":\"" . $lst[2] . "\",\"f\":null},{\"v\":" . $pos . ",\"f\":null},{\"v\":\"".$colours[$col]."\",\"f\":null} ]},";
	$col++;
    } else {
//      echo "{\"c\":[{\"v\":\"" . 'others' . "\",\"f\":null},{\"v\":" . $row['others'] . ",\"f\":null}]}, ";
    }
  }
  $c++;
}
  echo " ] }";
?>

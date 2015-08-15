<?php
$group = $_GET["q"];
//$group = "D";
$file = "seedings.csv";
$c=0;
$data=fopen($file,'r');
while($row=fgets($data)){
    //$row is your line as a string
    if($c!=0){
    //do something with it
    $lst = explode(",", $row);
	if ($lst[5]== $group){
    echo $lst[0] . "\t" . $lst[2] ."\t" . $lst[3]."\t" . $lst[4]. "\n";
	}
   }
   $c++;
}

?>

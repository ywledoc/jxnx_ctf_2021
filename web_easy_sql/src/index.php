<?php
$con = mysql_connect("127.0.0.1","root","root");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("supersqli", $con);

if(isset($_GET)){
	$_GET['id'] = 1;
}
$result = mysql_query("SELECT * FROM words where id=".$_GET['id']);

while($row = mysql_fetch_array($result))
  {
  echo $row['data'];
  echo "<br />";
  }

mysql_close($con);
?>
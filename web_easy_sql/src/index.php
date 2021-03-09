<?php
$con = mysqli_connect("127.0.0.1","root","root");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysqli_select_db("supersqli", $con);

if(isset($_GET)){
	$_GET['id'] = 1;
}
$result = mysqli_query("SELECT * FROM words where id=".$_GET['id']);

while($row = mysqli_fetch_array($result))
  {
  echo $row['data'];
  echo "<br />";
  }

mysqli_close($con);
?>

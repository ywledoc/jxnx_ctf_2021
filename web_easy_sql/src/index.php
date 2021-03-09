<?php
$con = mysqli_connect("", "root", "root", "supersqli", 0, "/run/mysqld/mysqld.sock");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysqli_select_db($con, "supersqli");

$id = isset($_GET['id']) ? $_GET['id'] : 1;

$result = mysqli_query($con,"SELECT * FROM words where id=".$id);

while($row = mysqli_fetch_array($result))
  {
  echo $row['data'];
  echo "<br />";
  }

mysqli_close($con);
?>

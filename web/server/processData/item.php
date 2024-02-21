<?php
include("../apiConnection.php");
$ch = curl_init();
$name = $_POST["name"];
$weight = $_POST["weight"];
$unity = $_POST["unity"];
$type = $_POST["type"];
$desc = $_POST["desc"];
$file = $_FILES["image"];
echo $url."/test";
curl_setopt($ch, CURLOPT_URL, $url."/test");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $name);
move_uploaded_file($file["tmp_name"], "./uploads/".$file["name"]);
 
?>

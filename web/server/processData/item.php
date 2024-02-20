<?php
$name = $_POST["name"];
$weight = $_POST["weight"];
$unity = $_POST["unity"];
$type = $_POST["type"];
$desc = $_POST["desc"];
$file = $_FILES["image"];
move_uploaded_file($file["tmp_name"], "./uploads/".$file["name"]); 
?>

<?php
include("../apiConnection.php");
$file = $_FILES["image"];
$url = API_URL."/test";

$data = array(
    "name" => $_POST["name"],
    "weight" => $_POST["weight"],
    "unity" => $_POST["unity"],
    "type" => $_POST["type"],
    "desc" => $_POST["desc"],
    "imgPath" => $_FILES["image"]["name"],
);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
curl_exec($ch);
 

?>
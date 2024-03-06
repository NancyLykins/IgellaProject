<?php
    include("../apiConnection.php");
    header("Content-type: application/json");
    session_start();
    $data = json_decode(file_get_contents("php://input"));
    $url = (string) API_URL."/characters/".$_SESSION["playerId"]."/inventary/".$data->itemId;
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_exec($ch);
    echo True;
?>
<?php
    include("../apiConnection.php");
    header("Content-type: application/json");
    session_start();
    $data = json_decode(file_get_contents("php://input"));
    $url = API_URL."/characters/".$_SESSION["playerId"]."/inventary/".$data->itemId;
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch. CURLOPT_CUSTOMREQUEST, "DELETE");
    curl_exec($ch);
?>
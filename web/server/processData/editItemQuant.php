<?php
    include("../apiConnection.php");
    header("Content-Type: application/json");
    session_start();
    $data = json_decode(file_get_contents("php://input", true));
    $ch = curl_init();
    $url = API_URL . "/characters/".$_SESSION["playerId"]."/inventary/".$data->itemId;
    $item = ["quant"=>$data->quant];
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PATCH');
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($item));
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_exec($ch);
    echo true;
?>
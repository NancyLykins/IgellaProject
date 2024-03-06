<?php
    include("../apiConnection.php");
    header("Content-Type: application/json");
    session_start();
    $data = json_decode(file_get_contents("php://input"), true);
    $item = (array) $data["item"];
    $url = (string) API_URL . "/itens/" . $item["name"];
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HTTPGET, 1);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    $response = (json_decode($response))[0];
    $rowId = (string) $response->rowId;
    $invItem = (array) [
        $rowId=>1,
    ];
    $ch = curl_init();
    $url = API_URL . "/characters/".$_SESSION["playerId"]."/inventary/".$rowId;
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($invItem));
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_exec($ch);
?>
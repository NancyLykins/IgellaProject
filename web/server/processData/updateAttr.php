<?php
    include("../apiConnection.php");
    //header('Content-Type: application/json');
    session_start();
    $data = json_decode(file_get_contents("php://input"), true);
    $id = (string) $_SESSION["playerId"];
    $url = (string) API_URL . "/characters/".$id."/status";
    $header = (array) ["Content-type: application/json"];
    $attr = $data["attr"];
    $body = (array) [
        $attr => "+1",
        "pontosRestantes" => "-1"
    ];
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PATCH');
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($body));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    curl_exec($ch);
    $response = (array) [
        "playerId"=>$id,
    ];
    echo json_encode($response);
?>
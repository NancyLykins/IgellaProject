<?php
include("../apiConnection.php");
$url = API_URL . "/item";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $weight = $_POST["weight"];
    $unity = $_POST["unity"];
    $type = $_POST["type"];
    $desc = $_POST["desc"];

    $file_path = $_FILES["image"]["tmp_name"];
    $file_name = $_FILES["image"]["name"];

    isset($_POST["action"])? $action = $_POST["action"]: $action = NULL;
    isset($_POST["bodySlot"])? $slot = $_POST["bodySlot"]: $slot = NULL;
    isset($_POST["time"])? $time = $_POST["time"]: $time = NULL;

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, [
        "name" => $name,
        "weight" => $weight,
        "unity" => $unity,
        "type" => $type,
        "desc" => $desc,
        "path" => "/itens",
        "emoji" => "🛡️",
        "action" => $action,
        "time" => $time,
        "slot" => $slot,
        "image" => new CURLFile($file_path, "", $file_name)
    ]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        echo 'Error: ' . curl_error($ch);
    } else {
        echo $response;
    }
    curl_close($ch);
} else {
    echo "Invalid request method.";
}
?>
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

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, [
        "name" => $name,
        "weight" => $weight,
        "unity" => $unity,
        "type" => $type,
        "desc" => $desc,
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

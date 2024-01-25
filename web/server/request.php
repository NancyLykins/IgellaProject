<?php
    require_once("apiConnection.php");
    $api = api;
    $crud = $_GET["crud"];
    $info = $_GET["info"];
    
    echo json_encode($crud);

?>
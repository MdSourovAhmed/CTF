<?php
session_start();
error_reporting(0);

if (!isset($_SESSION['dir'])) {
    $_SESSION['dir'] = random_bytes(4);
}

if (!isset($_GET['url'])) {
    die("Nope :<");
}

$include_url = basename($_GET['url']);
$SANDBOX = getcwd() . "/uploads/" . md5("supersafesalt!!!!@#$" . $_SESSION['dir']);

if (!file_exists($SANDBOX)) {
    mkdir($SANDBOX);
}

if (!file_exists($SANDBOX . '/' . $include_url)) {
    die("Nope :<");
}

if (!preg_match("/\.(zip|bz2|gz|xz|7z)/i", $include_url)) {
    die("Nope :<");
}

@include($SANDBOX . '/' . $include_url);
?>
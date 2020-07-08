<?php

$email      = $_POST["txtusername"];
$clave      = $_POST["txtclave"];

if($email == 'luisgp' && $clave === '12345')
{
    header("location: evaluacion.html");
}
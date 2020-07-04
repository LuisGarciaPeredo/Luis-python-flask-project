<?php

class Funciones {
    public static function mensaje($mensaje, $tipo, $archivoDestino="", $tiempo=0) {
            $estiloMensaje = "";
            
            if ($archivoDestino==""){
                $destino = "javascript:window.history.back();";
            }else{
                $destino = $archivoDestino;
            }
            
            $menuEntendido = '<div><a href="'.$destino.'">Entendido</a></div>';
            
            
            if ($tiempo==0){
                $tiempoRefrescar = 5;
            }else{
                $tiempoRefrescar = $tiempo;
            }
            
            switch ($tipo) {
                case "s":
                    $estiloMensaje = "alert callout-success";
                    $titulo = "Hecho";
                    break;
                
                case "i":
                    $estiloMensaje = "callout-info";
                    $titulo = "Información";
                    break;
                
                case "a":
                    $estiloMensaje = "callout-warning";
                    $titulo = "Cuidado";
                    break;
                
                case "e":
                    $estiloMensaje = "callout-danger";
                    $titulo = "Error";
                    break;

                default:
                    $estiloMensaje = "callout-info";
                    $titulo = "Información";
                    break;
            }
            
            $html_mensaje = '
                    <html>
                        <head>
                            <title>Mensaje del sistema</title>
                            <meta charset="utf-8">
                            <meta http-equiv="refresh" content="'.$tiempoRefrescar.';'.$destino.'">
                                
                            <link href="../util/bootstrap/css/bootstrap.css" rel="stylesheet" type="text/css" />
                            <!-- Theme style -->
                            <link href="../util/lte/css/AdminLTE.css" rel="stylesheet" type="text/css" />
    
    
                        </head>
                        <body>
                            <div class="containter">
                                <section class="content">
                                    <div class="callout '.$estiloMensaje.'">
                                        <h4>'.$titulo.'!</h4>
                                        <p>'.$mensaje.'</p>
                                    </div>
                                    '.$menuEntendido.'
                                </section>
                        </body>
                    </html>
                ';
            
            echo $html_mensaje;
            
            exit;
            
        }
}

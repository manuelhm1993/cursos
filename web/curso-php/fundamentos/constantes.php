<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP 8.3.x - Constantes</title>
</head>
<body>
    <?php 
        // Forma de trabajar con constantes globales
        define("AUTOR_LEGACY", "Manuel");

        echo "El autor del script es: " . AUTOR_LEGACY . "<br>";
        
        class Datos {
            // Forma moderna de declarar e inicializar constantes
            const AUTOR = "Ing. Manuel";
        }
            
        echo "El autor del script es: " . Datos::AUTOR . "<br>";
    ?>
</body>
</html>
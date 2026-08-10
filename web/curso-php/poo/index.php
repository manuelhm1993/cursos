<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP 8.3.x - POO</title>
</head>
<body>
    <?php 
        require_once "./Vehiculo.php";

        $mazda = new Vehiculo();

        echo $mazda->arrancar();
    ?>
</body>
</html>
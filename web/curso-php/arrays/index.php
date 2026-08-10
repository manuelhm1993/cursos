<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP 8.3.x - Destructuración de Arrays</title>
</head>
<body>
    <?php 
        function arrays_indexados(): void {
            $datos = [1, 2, 3];

            // Destructuración de arrays
            [$a, $b, $c] = $datos;

            echo "------ Variables destructurando el array Datos ------
            <br>- A: $a 
            <br>- B: $b 
            <br>- C: $c 
            ";
        }

        function arrays_asociativos(): void {
            $persona = [
                "Nombre" => "Manuel",
                "Edad"   => 33,
                "Ciudad" => "Maracaibo"
            ];

            // Destructuración de arrays asociativos
            [
                "Nombre" => $nombre, 
                "Edad"   => $edad, 
                "Ciudad" => $ciudad
            ] = $persona;

            echo "<br><br>------ Variables destructurando el array Persona ------
            <br>- Nombre: {$nombre} 
            <br>- Edad:   {$edad} 
            <br>- Ciudad: {$ciudad} 
            ";
        }

        arrays_indexados();
        arrays_asociativos();
    ?>
</body>
</html>
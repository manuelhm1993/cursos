<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP 8.3.x - Swtich, Lookup-table, Match</title>
</head>
<body>
    <?php 
        function uso_switch(int $estado): string {
            switch ($estado) {
                case 1:
                    $resultado = "Pendiente";
                    break;
                case 2:
                    $resultado = "En proceso";
                    break;
                case 3:
                    $resultado = "Completado";
                    break;
                default:
                    $resultado = "Desconocido";
                    break;
            }

            return $resultado;
        }

        function uso_look_up_table(int $estado): string {
            $estados = [
                1 => "Pendiente",
                2 => "En proceso",
                3 => "Completado"
            ];

            // Caso por defecto, usar el operador null coalesce operator
            $resultado = $estados[$estado] ?? "Desconocido";

            return $resultado;
        }

        function uso_match(int $estado): string {
            $resultado = match($estado) {
                1       => "Pendiente",
                2       => "En proceso",
                3       => "Completado",
                default => "Desconocido"
            };

            return $resultado;
        }

        $switch = uso_switch(2);
        $lookup = uso_look_up_table(2);
        $match  = uso_match(2);

        echo $match;
    ?>
</body>
</html>
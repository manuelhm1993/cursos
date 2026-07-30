<?php

/** Este es un script de ejemplo para un cron job
 * Conectarse a una base de datos, realizar una consulta, enviar un email, etc.
 * Por ejemplo, podríamos registrar la hora actual en un archivo
 * */ 

file_put_contents("/home/gdchvqhp/curso.mhenriquez.com/cron_log.txt", "Cron job ejecutado a las: " . date("Y-m-d H:i:s") . "\n", FILE_APPEND);

echo "Tarea ejecutada con éxito";

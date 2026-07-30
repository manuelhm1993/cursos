-- Todos los artículos de deportes que son americanos
SELECT *
FROM productos
WHERE LOWER(SECCION) = "deportes" AND LOWER(PAISDEORIGEN) = "usa";
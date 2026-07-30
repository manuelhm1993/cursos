-- Subconsulta escalonada: devuelve un registro de un único campo
-- Mostrar los artículos cuyo precio sea superior a la media
SELECT NOMBREARTICULO, SECCION, PRECIO
FROM productos
WHERE PRECIO > (SELECT AVG(PRECIO) FROM productos)
ORDER BY PRECIO ASC;
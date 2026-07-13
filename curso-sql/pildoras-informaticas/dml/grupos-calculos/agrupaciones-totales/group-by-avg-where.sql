-- Precio promedio de las secciones de cerámica y deportes
SELECT SECCION, AVG(PRECIO) AS PRECIO_MEDIO
FROM productos
GROUP BY SECCION
HAVING LOWER(SECCION) LIKE 'deportes' OR LOWER(SECCION) LIKE 'confecci_n'
ORDER BY PRECIO_MEDIO ASC;
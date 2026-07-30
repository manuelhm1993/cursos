-- Todos los artículos de cerámica y deportes
SELECT NOMBREARTICULO, SECCION, PRECIO 
FROM productos
WHERE LOWER(SECCION) = "cerámica" OR LOWER(SECCION) = "deportes";
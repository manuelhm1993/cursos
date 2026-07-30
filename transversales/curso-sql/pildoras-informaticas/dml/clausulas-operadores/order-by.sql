-- Todos los artículos de cerámica y deportes ordenados por sección
SELECT * FROM productos
WHERE SECCION = "DEPORTES" OR SECCION = "CERÁMICA"
ORDER BY SECCION ASC, PRECIO DESC;
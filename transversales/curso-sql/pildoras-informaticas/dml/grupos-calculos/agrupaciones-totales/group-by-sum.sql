-- Consultas de agrupaciones totales y funciones de agregado
SELECT SECCION, SUM(PRECIO) AS TOTAL
FROM productos
GROUP BY SECCION
ORDER BY TOTAL ASC;
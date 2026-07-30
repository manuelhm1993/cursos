-- Cuál es el artículo más caro de la sección de confección
SELECT SECCION, MAX(PRECIO) AS ART_MAS_CARO
FROM productos
GROUP BY SECCION
HAVING SECCION LIKE 'CONFECCIÓN';
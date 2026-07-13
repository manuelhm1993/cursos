-- Mostrar los artículos de la tabla de productos cuyo precio sea superior a 500 y los artículos de la tabla productos_nuevos cuya sección sea alta costura
SELECT * FROM productos p WHERE p.PRECIO > 500
UNION
SELECT * FROM productos_nuevos pn WHERE pn.seccion LIKE '%COSTURA%';
-- Una vez creada la tabla productos_nuevos con DCL y poblada con DML se procede a trabajar
-- Mostrar todos los productos de las secciones de deportes tanto nuevos como viejos sin duplicar la información
SELECT * FROM productos p WHERE p.SECCION LIKE 'DEPORTES'
UNION 
SELECT * FROM productos_nuevos pn WHERE pn.seccion LIKE 'DEPORTES%';
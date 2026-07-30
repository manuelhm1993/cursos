-- Prueba de union all, simplemente une ambas tablas y no elimina registros duplicados
SELECT * FROM productos p WHERE p.SECCION LIKE 'DEPORTES'
UNION ALL
SELECT * FROM productos_nuevos pn;
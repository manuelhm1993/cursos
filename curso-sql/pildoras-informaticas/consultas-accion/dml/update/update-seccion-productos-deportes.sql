-- Renombrar la sección de DEPORTES a DEPORTIVOS
SELECT * FROM productos;

UPDATE productos p
SET p.SECCION = 'DEPORTIVOS'
WHERE p.SECCION LIKE 'DEPORTES';

SELECT * FROM productos;
-- Actualzar en $10 hacia abajo todos los productos de la sección de deportes
SELECT * FROM productos;

UPDATE productos p 
SET p.PRECIO = p.PRECIO - 10
WHERE p.SECCION LIKE 'DEPORTES';

SELECT * FROM productos;
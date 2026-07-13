SELECT * FROM productos_nuevos;

INSERT INTO productos_nuevos
SELECT * FROM productos p WHERE p.CODIGOARTICULO = 'AR06';

SELECT * FROM productos_nuevos;
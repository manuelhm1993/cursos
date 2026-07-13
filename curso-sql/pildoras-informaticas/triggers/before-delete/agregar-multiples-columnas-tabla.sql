ALTER TABLE productos_eliminados
ADD COLUMN (usuario VARCHAR(255), fecha_borrado DATETIME);

SELECT * FROM productos_eliminados;
CREATE PROCEDURE update_precio_productos(precio DOUBLE(16,2), codigo_articulo VARCHAR(10))
	UPDATE productos p 
	SET p.PRECIO = precio
	WHERE p.CODIGOARTICULO = codigo_articulo;
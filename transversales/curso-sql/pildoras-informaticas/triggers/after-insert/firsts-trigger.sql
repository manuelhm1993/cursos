-- Crear un trigger asociado a productos donde por cada registro insertado se tiene un record en la tabla reg_productos
CREATE TRIGGER productos_ai
AFTER INSERT 
ON productos
FOR EACH ROW
	INSERT INTO reg_productos (codigo_art, nombre_art, precio, insertado)
	VALUES 
	(NEW.CODIGOARTICULO, NEW.NOMBREARTICULO, NEW.PRECIO, NOW());
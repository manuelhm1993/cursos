-- Crear trigger que permita hacer un respaldo de los productos eliminados
CREATE TRIGGER productos_ad
AFTER DELETE 
ON productos
FOR EACH ROW 
	INSERT INTO productos_eliminados (c_art, nombre, seccion, precio, pais_origen)
	VALUES 
	(OLD.CODIGOARTICULO, OLD.NOMBREARTICULO, OLD.SECCION, OLD.PRECIO, OLD.PAISDEORIGEN);
DROP TRIGGER IF EXISTS productos_ad;

CREATE TRIGGER IF NOT EXISTS productos_ad
AFTER DELETE 
ON productos
FOR EACH ROW 
	INSERT INTO productos_eliminados (c_art, nombre, seccion, precio, pais_origen, usuario, fecha_borrado)
	VALUES 
	(OLD.CODIGOARTICULO, OLD.NOMBREARTICULO, OLD.SECCION, OLD.PRECIO, OLD.PAISDEORIGEN, USER(), NOW());
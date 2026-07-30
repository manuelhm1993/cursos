-- Crear un trigger que sea capaz de hacer un respaldo del registro actualizado, guarde esos campos en productos_actualizados y sus valores nuevos, con la fecha y el usuario
CREATE TRIGGER productos_bu
BEFORE UPDATE
ON productos
FOR EACH ROW
	INSERT INTO productos_actualizados (
		codigo_articulo_old, codigo_articulo_new, 
		seccion_old, seccion_new, 
		nombre_articulo_old, nombre_articulo_new, 
		precio_old, precio_new, 
		fecha_old, fecha_new, 
		importado_old, importado_new, 
		pais_origen_old, pais_origen_new, 
		usuario, fecha_update
	)
	VALUES (
		OLD.CODIGOARTICULO, NEW.CODIGOARTICULO,
		OLD.SECCION, NEW.SECCION,
		OLD.NOMBREARTICULO, NEW.NOMBREARTICULO,
		OLD.PRECIO, NEW.PRECIO,
		OLD.FECHA, NEW.FECHA,
		OLD.IMPORTADO, NEW.IMPORTADO,
		OLD.PAISDEORIGEN, NEW.PAISDEORIGEN,
		USER(), NOW()
	);
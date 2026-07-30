-- crear tabla de respaldo para productos
DROP TABLE IF EXISTS productos_actualizados;

CREATE TABLE IF NOT EXISTS productos_actualizados (
	codigo_articulo_old VARCHAR(4),
	codigo_articulo_new VARCHAR(4),
	seccion_old			  VARCHAR(15),
	seccion_new			  VARCHAR(15),
	nombre_articulo_old VARCHAR(25),
	nombre_articulo_new VARCHAR(25),
	precio_old 			  DOUBLE(16,2),
	precio_new 			  DOUBLE(16,2),
	fecha_old			  DATE,
	fecha_new			  DATE,
	importado_old		  BIT,
	importado_new		  BIT,
	pais_origen_old	  VARCHAR(15),
	pais_origen_new	  VARCHAR(15),
	usuario				  VARCHAR(15),
	fecha_update		  DATETIME
) ENGINE INNODB;

SELECT * FROM productos_actualizados;
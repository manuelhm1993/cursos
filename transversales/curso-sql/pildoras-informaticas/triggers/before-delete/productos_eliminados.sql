DROP TABLE IF EXISTS productos_eliminados;

CREATE TABLE IF NOT EXISTS productos_eliminados (
	c_art     	VARCHAR(5),
	nombre    	VARCHAR(15),
	seccion   	VARCHAR(15),
	precio    	DOUBLE(16,2),
	pais_origen VARCHAR(15)
) ENGINE INNODB;

SELECT * FROM productos_eliminados;
-- Tabla para almacenar los datos de inserción de productos
DROP TABLE IF EXISTS reg_productos;

CREATE TABLE IF NOT EXISTS reg_productos (
	codigo_art VARCHAR(25),
	nombre_art VARCHAR(30),
	precio 	  DOUBLE(16,2),
	insertado  DATETIME
) ENGINE = INNODB;
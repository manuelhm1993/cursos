-- Eliminar una tabla si existe
DROP TABLE IF EXISTS prueba;

-- Crear una tabla si no existe
CREATE TABLE IF NOT EXISTS prueba (
	id					  BIGINT PRIMARY KEY AUTO_INCREMENT,
	nombre   		  VARCHAR(20),
	apellido 		  VARCHAR(20),
	edad				  TINYINT,
	fecha_nacimiento DATE,
	carnet			  BIT
) ENGINE INNODB;

SELECT * FROM prueba;
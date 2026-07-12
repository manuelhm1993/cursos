-- Crear tabla para el ejemplo de índices DCL
DROP TABLE IF EXISTS indexes_tests;

CREATE TABLE IF NOT EXISTS indexes_tests (
	dni 	   VARCHAR(255),
	nombre   VARCHAR(255),
	apellido VARCHAR(255),
	edad		INTEGER,
	PRIMARY KEY (dni)
);
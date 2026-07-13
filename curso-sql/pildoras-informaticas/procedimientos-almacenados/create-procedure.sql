-- Crear un procedimiento almacenado DDL
-- Los procedimientos pueden recibir parámetros tal como una función
CREATE PROCEDURE clientes_madrid()
	SELECT * FROM clientes c WHERE c.POBLACION LIKE 'MADRID';
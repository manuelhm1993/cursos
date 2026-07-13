-- Consultas de creación de tabla DDL
DROP TABLE IF EXISTS clientes_madrid;

CREATE TABLE IF NOT EXISTS clientes_madrid 
SELECT * FROM clientes 
WHERE POBLACION = 'MADRID';

SELECT * FROM clientes_madrid;
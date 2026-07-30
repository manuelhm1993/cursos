DROP TABLE IF EXISTS clientes_nuevos;

CREATE TABLE IF NOT EXISTS clientes_nuevos (
	codigo_cliente VARCHAR(10),
	empresa VARCHAR(30),
	direccion VARCHAR(20),
	poblacion VARCHAR(10),
	telefono VARCHAR(50),
	responsable VARCHAR(40),
	historial TEXT
) ENGINE=INNODB;

INSERT INTO clientes_nuevos
SELECT * FROM clientes_madrid;

INSERT INTO clientes_nuevos
SELECT * FROM clientes c WHERE c.POBLACION NOT LIKE 'MADRID';

SELECT * FROM clientes_nuevos;
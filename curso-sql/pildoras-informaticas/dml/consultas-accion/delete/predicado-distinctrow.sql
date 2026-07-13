-- Uso de distinctrow para eliminar redundancias de registros completos
SELECT * FROM clientes_madrid;

INSERT INTO clientes_madrid
SELECT * FROM clientes_madrid WHERE CODIGOCLIENTE = 'CT39';

SELECT * FROM clientes_madrid;
SELECT DISTINCTROW * FROM clientes_madrid;
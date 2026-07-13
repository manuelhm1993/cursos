-- Subconsulta de lista: devuelve una  lista de registros registro
-- IN:     operador (predicado) que permite indicar que el criterio devuelva true si existe en un registro de la columna devualta en la subconsulta
-- NOT IN: operador (predicado) que permite indicar que el criterio devuelva true no existe en un registro de la columna devualta en la subconsulta
-- Devolver todos lo artículos que su precio sea superior a todos los artículos de la sección de cerámica
SELECT p.NOMBREARTICULO, p.PRECIO 
FROM productos p
WHERE p.CODIGOARTICULO IN (SELECT pp.CODIGOARTICULO FROM productos_pedidos pp WHERE pp.UNIDADES > 20);

-- Testing y comparativa de código
SELECT CODIGOARTICULO, SUM(UNIDADES) AS unidades FROM productos_pedidos GROUP BY CODIGOARTICULO HAVING unidades > 20 ORDER BY unidades DESC;
SELECT * FROM productos_pedidos WHERE unidades > 20 ORDER BY unidades DESC;
SELECT * FROM productos_pedidos WHERE CODIGOARTICULO = 'AR12'
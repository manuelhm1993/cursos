-- Subconsulta de lista: devuelve una  lista de registros registro
-- IN:     operador (predicado) que permite indicar que el criterio devuelva true si existe en un registro de la columna devualta en la subconsulta
-- NOT IN: operador (predicado) que permite indicar que el criterio devuelva true no existe en un registro de la columna devualta en la subconsulta
-- Devolver el nombre y precio de los artículos de loc cuales se han pedido más de 20 unidades
SELECT p.NOMBREARTICULO, p.PRECIO
FROM productos p
WHERE p.CODIGOARTICULO IN (SELECT pp.CODIGOARTICULO FROM productos_pedidos pp GROUP BY pp.CODIGOARTICULO HAVING SUM(pp.UNIDADES) > 20)
ORDER BY p.PRECIO DESC
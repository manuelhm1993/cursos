-- Subconsulta de lista: devuelve una  lista de registros registro
-- Devolver todos lo artículos que su precio sea superior a todos los artículos de la sección de cerámica
-- ANY: operador que permite indicar que el criterio devuelva true si coincide con cualquier registro de la lista
-- ALL: operador que permite indicar que el criterio devuelva true si coincide con todos los registros de la lista
SELECT * FROM productos p
WHERE p.PRECIO > ANY (SELECT p2.PRECIO FROM productos p2 WHERE LOWER(p2.SECCION) LIKE 'cerámica')
ORDER BY p.PRECIO DESC;
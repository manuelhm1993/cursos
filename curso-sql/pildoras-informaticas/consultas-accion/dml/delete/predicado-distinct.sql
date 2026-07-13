-- Empresas que han hecho pedidos. El predicado distinct se usa para eliminar redundancias en un campo específico
SELECT DISTINCT c.EMPRESA
FROM clientes c
INNER JOIN pedidos p
ON c.CODIGOCLIENTE = p.CODIGOCLIENTE;
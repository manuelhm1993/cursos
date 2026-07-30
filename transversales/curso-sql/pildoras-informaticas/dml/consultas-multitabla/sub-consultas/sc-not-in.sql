-- Clientes que no han pagado con tarjeta o que no han hecho pedidos
SELECT c.EMPRESA, c.POBLACION 
FROM clientes c 
WHERE c.CODIGOCLIENTE NOT IN (SELECT p.CODIGOCLIENTE FROM pedidos p WHERE p.FORMADEPAGO LIKE 'TARJETA');
-- Cuántos clientes hay por provincia, cclientesláusula group by y función de agregado count
SELECT POBLACION, COUNT(CODIGOCLIENTE) AS TOTAL_CLIENTES
FROM clientes
GROUP BY POBLACION
ORDER BY POBLACION;

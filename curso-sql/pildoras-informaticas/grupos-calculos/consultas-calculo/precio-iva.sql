-- Consultas de cálculo, no actuan sobre grupos, si no, sobre registros individuales
-- Calcular el IVA 21% sobre el campo precio de la tabla de productos
SELECT CODIGOARTICULO, SECCION,NOMBREARTICULO, PRECIO AS PRECIO_BRUTO, (PRECIO * 1.21) AS PRECIO_IVA
FROM productos
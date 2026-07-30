-- Crear vista para los artículos de deportes
CREATE VIEW art_deportes
AS 
	SELECT p.NOMBREARTICULO, p.SECCION, p.PRECIO
	FROM productos p
	WHERE p.SECCION LIKE 'DEPORTES';
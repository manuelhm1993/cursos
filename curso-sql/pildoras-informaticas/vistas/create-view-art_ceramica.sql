-- Crear vista para la sección de cerámica
CREATE VIEW art_ceramica
AS 
	SELECT p.NOMBREARTICULO, p.SECCION, p.PRECIO 
	FROM productos p
	WHERE p.SECCION LIKE 'CER_MICA';
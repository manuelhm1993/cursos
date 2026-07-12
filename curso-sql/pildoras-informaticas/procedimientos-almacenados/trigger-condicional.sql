-- Crear un procedimiento almacenado para un trigger condicional
DELIMITER $$
CREATE TRIGGER validar_precio_bu BEFORE UPDATE ON productos FOR EACH ROW	
	BEGIN 
		IF(NEW.PRECIO < 0) THEN
			SET NEW.PRECIO = 0;
		ELSEIF(NEW.PRECIO > 1000) THEN
			SET NEW.PRECIO = 1000;
		END IF;
	END;$$
DELIMITER ;
BEGIN
	DECLARE anio_actual INT DEFAULT 2026; -- Crear una variable con el año actual por defecto
	DECLARE edad INT;
	
	SET edad = anio_actual - anio_nacimiento; -- Establecer el valor de una variable
	
	SELECT edad; -- Equivalente de return (esto es una función)
END
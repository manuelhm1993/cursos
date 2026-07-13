-- Agregar un nuevo campo a una tabla existente
ALTER TABLE tb_clientes_madrid
ADD COLUMN fecha_baja DATE AFTER RESPONSABLE; -- Para especificar la ubicación se usa after o first

-- Eliminar una columna
ALTER TABLE tb_clientes_madrid
DROP COLUMN fecha_baja;
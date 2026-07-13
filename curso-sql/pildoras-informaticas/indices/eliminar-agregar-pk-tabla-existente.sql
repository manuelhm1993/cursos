-- Eliminar la PK de la tabla
ALTER TABLE indexes_tests DROP PRIMARY KEY;

-- Agregar la PK a la tabla
ALTER TABLE indexes_tests ADD PRIMARY KEY (dni);
-- Crear índice ordinario: permite nulos y duplicados, sirve para consultas más rápidas y para FK
CREATE INDEX io_apellido_indexes_tests ON indexes_tests (apellido);

-- Eliminar index usando drop
DROP INDEX io_apellido_indexes_tests ON indexes_tests;

-- Crear index usando alter
ALTER TABLE indexes_tests ADD INDEX io_apellido_indexes_tests (apellido);

-- Eliminar index usando alter
ALTER TABLE indexes_tests DROP INDEX io_apellido_indexes_tests;
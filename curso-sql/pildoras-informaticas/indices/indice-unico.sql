-- Crear índice único, no permite duplicados, pero si nulos
CREATE UNIQUE INDEX ui_apellido_indexes_tests ON indexes_tests (apellido);

-- Eliminar índice con drop
DROP INDEX ui_apellido_indexes_tests ON indexes_tests;

ALTER TABLE indexes_tests ADD UNIQUE INDEX ui_apellido_indexes_tests (apellido);

-- Eliminar índice, no se usa unique, simplemente index
ALTER TABLE indexes_tests DROP INDEX ui_apellido_indexes_tests;
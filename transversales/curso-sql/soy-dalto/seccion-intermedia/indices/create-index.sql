-- Los índices permiten marcar campos para optimizar las búsquedas, existen índices únicos, índices primarios PK y nulos FK
-- Creación de índice ordinario no único DCL
create index iProductName
on Products (ProductName);
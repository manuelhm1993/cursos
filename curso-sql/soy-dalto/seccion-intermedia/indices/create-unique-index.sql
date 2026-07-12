-- Los índices permiten marcar campos para optimizar las búsquedas, existen índices únicos, índices primarios PK y nulos FK
-- Creación de índice único compuesto, es decir, ningún usuario puede tener el mismo nombre y apellido a la vez. DCL
create unique index uciFirstNameLastName
on Employees (FirstName, LastName);
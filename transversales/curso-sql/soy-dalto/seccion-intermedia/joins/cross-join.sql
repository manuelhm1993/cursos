-- Los joins son consultas multitabla que permiten relacionar la información y crean una tabla resultado
-- Cross join implícito: cruza la información de dos tablas
select *
from Employees e, Orders o
where e.EmployeeID = o.EmployeeID; -- Con el where es un inner join implícito

-- Cross join explícito: cruza la información de dos tablas
select *
from Employees e
cross join Orders o
-- where e.EmployeeID = o.EmployeeID; -- Sin el where es un cross join que cruza toda la tabla 'a' con toda la tabla 'b'
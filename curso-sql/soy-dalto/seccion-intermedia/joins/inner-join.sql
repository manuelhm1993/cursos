-- Los joins son consultas multitabla que permiten relacionar la información y crean una tabla resultado
-- Inner join implícito: cruza la información de dos tablas y devuelve la coincidencia de ambas
select *
from Employees e, Orders o
where e.EmployeeID = o.EmployeeID;

-- Inner join clásico: ídem
select *
from Employees e
join Orders o
on e.EmployeeID = o.EmployeeID;

-- Inner join moderno: ídem
select *
from Employees e
inner join Orders o
on e.EmployeeID = o.EmployeeID;
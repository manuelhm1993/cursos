-- Union: es cláusula que se usa en SQL para combinar 2 o más tablas que deben ser compatibles en número de campos y tipo
-- si existen registros duplicados, son agrupados y muestra solo el primero
-- Union all: ídem union, pero no agrupa, devuelve TODO, incluyendo duplicados
select e.FirstName, r.Reward, r.Month
from Employees e
right join Rewards r
on e.EmployeeID = r.EmployeeID 

union
--union all

select e.FirstName, r.Reward, r.Month
from Employees e
left join Rewards r
on e.EmployeeID = r.EmployeeID; 
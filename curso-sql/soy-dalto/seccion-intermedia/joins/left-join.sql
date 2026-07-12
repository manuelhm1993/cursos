-- Devolver los empleados y mostrar si han tenido o no recompensas por productividad
select e.FirstName, r.Reward, r.Month
from Employees e
left join Rewards r
on e.EmployeeID = r.EmployeeID
order by Reward asc nulls last; -- En ordenamientos se puede manipular si los nulos van al principio o al final

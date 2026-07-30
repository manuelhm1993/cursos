-- Devolver las recompensas por productividad si tienen o no trabajadores asociados
select e.FirstName, r.Reward, r.Month
from Employees e
right join Rewards r
on e.EmployeeID = r.EmployeeID
order by Reward asc nulls last; 

-- En versiones anteriores de sqlite no estaba soportado el right join, entonces se simulaba cambiando el sentido del left
select e.FirstName, r.Reward, r.Month
from Rewards r
left join Employees e
on r.EmployeeID = e.EmployeeID
order by Reward asc nulls last; 
-- Right join
select e.FirstName, r.Reward, r.Month
from Employees e
right join Rewards r
on e.EmployeeID = r.EmployeeID 

-- Full join: une dos joins que deben coincidir en campos y tipo
union

-- Left join
select e.FirstName, r.Reward, r.Month
from Employees e
left join Rewards r
on e.EmployeeID = r.EmployeeID; 
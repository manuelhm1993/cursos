select e.EmployeeID, e.FirstName, e.LastName, e.BirthDate, (
	select sum(od.Quantity) 
	from Orders o, OrderDetails od
	where o.EmployeeID = e.EmployeeID and o.OrderID = od.OrderID
) as unidades_vendidas
from Employees e
where unidades_vendidas > (
	select avg(prom_ventas.unidades_vendidas)
	from (
		select (
			select sum(od2.Quantity) 
			from Orders o2, OrderDetails od2
			where o2.EmployeeID = e2.EmployeeID and o2.OrderID = od2.OrderID
		) as unidades_vendidas 
		from Employees e2
	) prom_ventas
)
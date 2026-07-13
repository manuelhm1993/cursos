-- Ejercicio práctico de subconsultas: determinar cuáles son los empleados que vendieron más unidades que el promedio
select e.EmployeeID, e.FirstName, e.LastName, e.BirthDate, (
	select sum(Quantity) 
	from OrderDetails od 
	where od.OrderID in (select OrderID from Orders o where o.EmployeeID = e.EmployeeID)
) as unidades_vendidas
from Employees e
where unidades_vendidas > (
	select avg(prom_ventas.unidades_vendidas)
	from (
			select EmployeeID,
				sum((select sum(od2.Quantity) from OrderDetails od2 where od2.OrderID = o2.OrderID)) as unidades_vendidas
			from Orders o2
			group by EmployeeID
		) prom_ventas
)
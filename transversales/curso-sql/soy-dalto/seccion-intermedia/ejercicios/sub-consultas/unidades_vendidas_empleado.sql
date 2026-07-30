-- Ejercicio práctico de subconsultas: determinar cuáles son los empleados que vendieron más unidades que el promedio
select EmployeeID,
	sum((select sum(Quantity) from OrderDetails od where od.OrderID = o.OrderID)) as unidades_vendidas
from Orders o
group by EmployeeID
order by unidades_vendidas desc
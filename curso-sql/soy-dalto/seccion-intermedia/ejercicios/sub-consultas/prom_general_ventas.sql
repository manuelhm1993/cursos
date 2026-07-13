select round(avg(tmp.unidades_vendidas), 2) as prom_ventas from (select EmployeeID,
	sum((select sum(Quantity) from OrderDetails od where od.OrderID = o.OrderID)) as unidades_vendidas
from Orders o
group by EmployeeID) tmp
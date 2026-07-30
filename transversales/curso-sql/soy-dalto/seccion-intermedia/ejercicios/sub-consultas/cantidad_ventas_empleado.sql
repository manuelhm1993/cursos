-- Ejercicio práctico de subconsultas: determinar cuáles son los empleados que vendieron más unidades que el promedio
select EmployeeID, count(OrderID) as cantidad_ventas
from Orders o
group by EmployeeID
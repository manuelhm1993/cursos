-- Una subconsulta siempre debe ser un select, no alteran la db, siempre devuelven información
-- Dime la cantidad vendida por producto, el total recaudado y el nombre del producto
select 
	od.ProductID, sum(od.Quantity) as cantidad_vendida, 
	(select p.Price from Products p where p.ProductID = od.ProductID) as Price,
	((select p.Price from Products p where p.ProductID = od.ProductID) * sum(od.Quantity)) as total_recaudado,
	(select p.ProductName from Products p where p.ProductID = od.ProductID) as ProductName
from 
	OrderDetails od
where 
	Price > 40
group by 
	od.ProductID
order by 
	total_recaudado desc
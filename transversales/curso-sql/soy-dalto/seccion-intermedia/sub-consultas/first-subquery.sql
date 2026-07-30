-- Una subconsulta siempre debe ser un select, no alteran la db, siempre devuelven información
-- Cantidad de producto vendida con su nombre y precio
select 
	ProductID, 	
	Quantity,
	(select ProductName from Products p where p.ProductID = od.ProductID) as ProductName,
	(select Price from Products p where p.ProductID = od.ProductID) as Price
from OrderDetails od;
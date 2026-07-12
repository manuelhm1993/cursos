-- Rendimiento de esta consulta 25ms sin índices
select * 
from OrderDetails od
inner join Orders o
on od.OrderID = o.OrderID
where o.OrderDate > '1996-07-04' and od.Quantity > 10;

-- Creación de índices
create index iQuantity  on OrderDetails (Quantity);
create index iOrderDate on Orders (OrderDate);

-- Rendimiento de esta consulta 25ms con índices. No hubo mejora al aplicarlos
select * 
from OrderDetails od
inner join Orders o
on od.OrderID = o.OrderID
where o.OrderDate > '1996-07-04' and od.Quantity > 10;

-- Borrado de índices
drop index iQuantity;
drop index iOrderDate;
-- ¿Cuál es el producto de más se vende?
select cantidad_producto.ProductID, max(cantidad_producto.cantidad_vendida) as mas_vendido
from 
(select ProductID, sum(Quantity) as cantidad_vendida 
from OrderDetails
group by ProductID
order by cantidad_vendida desc) as cantidad_producto
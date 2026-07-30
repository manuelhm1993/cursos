-- La cláusula having permite agregar condiciones a un grupo, equivalente de where
-- Traer el promedio de los productos por proveedor
select SupplierID, round(avg(Price), 2) as media_producto
from Products
where ProductName is not null
group by SupplierID
having media_producto > 40
order by media_producto;
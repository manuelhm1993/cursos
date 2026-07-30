-- Productos que no pertenecen a la categoria 6, no son del proveedor 1, el precio es <= 30 y son 3 registros aleatorios
select *
from Products
where 
not CategoryID = 6
and 
not SupplierID = 1
and Price <= 30
order by random()
limit 3
-- El operador in permite realizar consultas para comparar un valor con un grupo de valores. 
-- Productos de una lista de proveedores
select * 
from Products
where SupplierID in (3, 4, 5, 6)
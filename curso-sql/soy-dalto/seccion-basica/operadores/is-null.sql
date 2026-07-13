-- Is null e is not null son operadores que permiten manipular valores nulos. Mostrar los productos que tengan nombre
select * 
from Products
where ProductName is not null
order by ProductName asc;
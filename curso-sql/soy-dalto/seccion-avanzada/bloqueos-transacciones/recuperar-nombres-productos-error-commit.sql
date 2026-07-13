-- Se hizo una mala transacción y se cambiaron todos los nombres por no dejarla abierta, se creó una tabla tmp para
-- recuperar los nombres
select * from tmp;
select ProductID, ProductName from Products;

-- El inner join muestra que las tablas coinciden
select p.ProductID, p.ProductName, t.id, t.nombre
from Products p
inner join tmp t
on p.ProductID = t.id;

-- Update inner
UPDATE Products
SET ProductName = (
    SELECT t.nombre 
    FROM tmp t 
    WHERE t.id = Products.ProductID
)
WHERE EXISTS (
    SELECT 1 
    FROM tmp t 
    WHERE t.id = Products.ProductID
);

-- Comprobar funcionamiento
select * from Products;
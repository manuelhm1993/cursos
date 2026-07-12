-- Consultas de agrupación con funciones de agregado
-- Traer el promedio de los productos por categoría
select CategoryID, round(avg(Price), 2) as precio_medio
from Products
where CategoryID is not null
group by CategoryID
order by CategoryID asc;
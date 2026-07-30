-- ¿Cuál es el producto de más se vende?
select ProductID, sum(Quantity) as cantidad_vendida 
from OrderDetails
group by ProductID
order by cantidad_vendida desc
limit 1
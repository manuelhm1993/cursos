select * 
from Customers
where 
CustomerID >= 50 
and 
(not lower(Country) like "germany" and not lower(Country) like "uk" and not lower(Country) like "argentina")
limit 5; -- Permite delimitar la cantidad de registros a mostrar
select distinct ProductName, Price, Unit -- DISTINCT se coloca después del select y elimina duplicados en la consulta
from Products
order by ProductName asc;
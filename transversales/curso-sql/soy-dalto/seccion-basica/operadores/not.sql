select *
from Customers
where not lower(Country) = "usa"; -- Operador not para negar un resultado
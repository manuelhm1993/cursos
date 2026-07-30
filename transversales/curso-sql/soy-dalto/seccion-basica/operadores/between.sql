-- Uso del operador BETWEEN para trabajar con rangos de fechas
select * 
from Employees
where BirthDate between '1960-01-01' and '1970-12-31';
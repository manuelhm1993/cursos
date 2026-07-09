-- Operador like, permite comparar por defecto como =, pero se potencia con caracteres comodín % y _
select * 
from Employees
-- where lower(LastName) like '%er%' -- Cualquier cosa antes y después de 'er'
where lower(LastName) like 'f____r'  -- Inicia con 'f', termina con 'r' y tiene 4 caracteres en medio
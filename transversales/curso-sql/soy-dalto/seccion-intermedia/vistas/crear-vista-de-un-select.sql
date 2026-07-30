-- Eliminar una vista
drop view if exists productos_simplificados;

-- Creación de vistas: son objetos que encapsulan el resultado de una consulta
create view if not exists productos_simplificados 
as
	select p.ProductID, p.ProductName, p.Price
	from Products p
	where ProductID > 20
	order by ProductID desc;

-- Llamar a una vista
select * from productos_simplificados;
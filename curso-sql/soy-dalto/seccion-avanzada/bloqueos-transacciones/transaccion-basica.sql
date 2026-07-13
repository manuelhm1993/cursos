begin transaction; -- Las transacciones no pueden iniciar con comentarios
	update Products set ProductName = 'Tazón' where ProductName like 'Manuel';
commit -- El commit funciona como end transaction;
-- rollback -- Si ocurre un error, el rollback elimina todos los cambios de la transacción
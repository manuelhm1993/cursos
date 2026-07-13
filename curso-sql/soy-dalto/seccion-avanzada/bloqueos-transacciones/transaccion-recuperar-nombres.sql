BEGIN TRANSACTION;
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
COMMIT
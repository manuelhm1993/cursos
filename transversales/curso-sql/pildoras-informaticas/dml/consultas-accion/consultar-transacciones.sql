SELECT 
	trx_id, 
	trx_state, 
	trx_started, 
	trx_mysql_thread_id, 
	trx_query 
FROM information_schema.INNODB_TRX 
ORDER BY trx_started ASC;
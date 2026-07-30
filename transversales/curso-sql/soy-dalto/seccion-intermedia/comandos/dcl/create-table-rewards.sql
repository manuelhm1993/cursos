-- DCL: data, creation, language
-- Comando para crear una nueva db, tabla o algún otro objeto
create table if not exists Rewards (
	RewardID   integer,
	EmployeeID integer,
	Reward     integer,
	Month	   text,
	primary key(RewardID autoincrement)
);

-- DML: data, manipulation, language
-- Comando para insertar registros y poblar una tabla
insert into Rewards (EmployeeID, Reward, Month)
values 
(3, 200, "January"),
(2, 180, "February"),
(5, 250, "March"),
(1, 280, "April"),
(8, 160, "May"),
(null, null, "June");
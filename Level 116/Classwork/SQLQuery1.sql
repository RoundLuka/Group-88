-- create database goa;

-- use goa;

create table aura (
	id INT primary key IDENTITY(1,1) NOT NULL,
	username VARCHAR(25),
	questions INT,
	pushup INT,
	classwork INT,
)

--insert into aura  values 
--('etew', 26, 35, 4220),
--('wreyrtyu', 4, 22, 20)

select * from aura order by classwork desc;
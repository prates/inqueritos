show databases;

create database inqueritos;

use inqueritos;

show tables;


create table inquerito(
id integer primary key,
bandido varchar(80),
vitima varchar(80),
data_abertura datetime,
data_vencimento datetime
)



create table relacionamento_inquerito_delegado(
id_inquerito integer,
id_delegado integer,
FOREIGN KEY (id_inquerito) REFERENCES inquerito(id),
FOREIGN KEY (id_delegado) REFERENCES delegado(id)
)

create table delegado(
 id integer primary key,
 nome varchar(80),
 dp integer
)


describe inquerito;

alter table inquerito change column data_venciamento data_vencimento varchar(80);

drop table inquerito;

insert into inquerito 
	(id, 
	bandido, 
	vitima, 
	data_abertura, 
	data_vencimento) values
	(5, 'Trump', 'Sao joe Biden', '2020-03-22 12:23:12', 
	'2020-04-22 12:23:12' );

select bandido, count(*) as 'processos' from inquerito group by bandido;

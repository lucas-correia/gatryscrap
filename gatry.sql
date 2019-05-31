create table promotion (
id int primary key auto_increment,
identifier varchar(15) unique,
name varchar(255) not null,
url varchar(500),
gatry_url varchar(500),
price varchar(12)
);
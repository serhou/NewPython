select * from user_t;
select * from web;
select * from weather;
create table userInfo (
	id bigint(18) NOT NULL,
	name varchar(40) NOT NULL,
	info varchar(255),
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
insert into userInfo values(1,'张三丰','一代太极宗师');
insert into userInfo values(2,'鲁迅','一个斗士，一代文学巨将');
insert into userInfo values(3,'蒋介石','一代枭雄');

create database igella;

drop table characters;
drop table map_elements;
drop table elements;
drop table maps;
drop table campaigns;
drop table accounts;


create table accounts(
    id serial primary key,
    name varchar(45) not null unique,
    email varchar(255) not null unique,
    password text not null,
    discord_id varchar(255)
);


create table campaigns(
    id serial primary key,
    title varchar(45) not null,
    description text,
    sistem varchar(45) not null,
    started date default Now(),
    server_id varchar(255),
    master int not null references accounts(id)
);


create table maps(
    id serial primary key,
    name varchar(45) not null,
    description text,
    cover varchar(255),
    campaign_id int not null references campaigns(id)
);


create table elements(
    id serial primary key,
    name varchar(45) not null,
    description text,
    img varchar(255) not null,
    public bool default false,
    creator int not null references accounts(id)
);


create table map_elements(
    id serial primary key,
    positionX int not null,
    positionY int not null,
    width int not null,
    heigth int not null,
    z_index int default 0,
    rotate int default 0,
    element_id int not null references elements(id),
    map_id int not null references maps(id)
);


create table characters(
    id serial primary key,
    sheet_id varchar(255) not null unique,
    campaigns_id int not null references campaigns(id),
    owner_id int not null references accounts(id)
);


insert into accounts(name, email, password) values('admin', 'admin@admin.com', 'admin');
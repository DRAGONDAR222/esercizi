create database esami;
\c esami

create domain posint as integer
    check (value > 0);

create domain


create type indirizzo as(
    via varchar(100),
    cap char(5),
    civico posint_not_null
)

create table docente(
    mat integer primary key,
    cognome varchar(100) not null,
    nome varchar(100) not null,
    email varchar(100) not null
);

create table corso(
    codice integer primary key,
    nome varchar not null,
    aula varchar(100) not null
);

create table incarico(
    docente integer not null,
    corso integer not null,
    primary key(docente, corso),
    foreign key (docente)
        references docente(mat),
    foreign key (corso)
        references corso(codice)
);



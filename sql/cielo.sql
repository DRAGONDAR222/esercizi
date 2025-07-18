-- create database cielo;

-- \c cielo

create domain Posinteger as integer
    check (value > 0);

create domain StringaM as varchar(100);

create domain CodIATA as char(3);

create table Volo(
    codice Posinteger not null,
    comp StringaM not null,
    durataMinuti Posinteger not null,
    primary key(codice,comp),
    foreign key (comp)
        references Compagnia(nome),
); 

create table ArrPart(
    codice Posinteger not null,
    comp StringaM not null,
    arrivo CodIATA not null,
    partenza CodIATA not null,
    primary key(codice,comp),
    foreign key(codice,comp)
        references Volo(codice,comp),
    foreign key(arrivo)
        references Aeroporto(codice),
    foreign key(partenza)
        references Aeroporto(codice)
);

create table Aeroporto(
    codice CodIATA primary key,
    nome StringaM not null,
    foreign key (codice) 
        references LuogoAeroporto(aeroporto)
);

create table LuogoAeroporto(
    aeroporto CodIATA primary key,
    citta StringaM not null,
    nazione StringaM not null,
    foreign key (aeroporto)
        references Aeroporto(codice)
);

create table Compagnia(
    nome StringaM primary key,
    annoFondaz Posinteger
);


select

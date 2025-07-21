-- create database cielo;

-- \c cielo

create domain Posinteger as integer
    check (value >= 0);

create domain StringaM as varchar(100);

create domain CodIATA as char(3);


create table LuogoAeroporto(
    aeroporto CodIATA primary key,
    citta StringaM not null,
    nazione StringaM not null
);

create table Aeroporto(
    codice CodIATA primary key,
    nome StringaM not null,
    foreign key (codice) 
        references LuogoAeroporto(aeroporto) deferrable
);

create table Compagnia(
    nome StringaM primary key,
    annoFondaz Posinteger
);

create table ArrPart(
    codice Posinteger not null,
    comp StringaM not null,
    arrivo CodIATA not null,
    partenza CodIATA not null,
    primary key(codice,comp),
    foreign key(arrivo)
        references Aeroporto(codice)
);

create table Volo(
    codice Posinteger not null,
    comp StringaM not null,
    durataMinuti Posinteger not null,
    primary key(codice,comp),
    foreign key (comp)
        references Compagnia(nome),
    foreign key (codice,comp)
        references ArrPart(codice,comp) deferrable
); 


alter table LuogoAeroporto 
add foreign key (aeroporto)
references Aeroporto(codice) deferrable;

alter table ArrPart
add foreign key(codice,comp)
references Volo(codice,comp) deferrable;


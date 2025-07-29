-- CREATE DATABASE ordini_e_fatture

-- \c ordini_e_fatture


-- Tipi di dato non standard

CREATE DOMAIN Stringa AS varchar(255);

CREATE DOMAIN RealGEZ AS real
CHECK (value >= 0);

CREATE DOMAIN RealZO AS real
CHECK (value IN (0,1));

CREATE DOMAIN posinteger AS integer
CHECK (value >= 0);

CREATE TYPE Indirizzo AS (
  via Stringa,
  civico Stringa,
  CAP integer
);

CREATE DOMAIN CodiceFiscale AS char(16);

CREATE DOMAIN PartitaIVA AS char(11)
CHECK (value ~ '^[0-9]{11}$');

CREATE DOMAIN Telefono AS varchar(20)
CHECK (value ~ '^\+?[0-9\s\-\(\)]{6,20}$');

CREATE DOMAIN Email AS varchar(254)
CHECK (value ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

CREATE TYPE stato AS ENUM (
  'in preparazione',
  'inviato',
  'da saldare',
  'saldato'
);

create table nazione(
    nome Stringa primary key
);

create table regione(
    nome Stringa not null,
    nazione Stringa not null,
    primary key(nome,nazione),
    foreign key(nazione)
        references nazione(nome)
);

create table citta(
    id integer primary key,
    nome Stringa not null,
    regione Stringa not null,
    nazione Stringa not null,
    unique (nome,regione,nazione),
    foreign key(regione,nazione)
        references regione(nome,nazione)
);

create table Direttore(
    nome Stringa not null,
    cognome Stringa not null,
    cf CodiceFiscale primary key,
    data_nascita date,
    anni_servizio posinteger not null,
    citta integer not null,
    foreign key(citta)
        references citta(id)
);

create table Dipartimento(
    nome Stringa primary key,
    indirizzo Indirizzo not null,
    direttore CodiceFiscale not null,
    foreign key (direttore)
        references Direttore(cf)
);


create table Fornitore(
    ragione_sociale Stringa not null,
    partitaIVA PartitaIVA primary key,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null
);

create table Ordine(
    id integer primary key,
    data_stipula date not null,
    imponibile RealGEZ not null,
    aliquotaIVA RealZO not null,
    descrizione Stringa not null,
    stato stato not null,
    fornitore PartitaIVA not null,
    dipartimento Stringa not null,
    foreign key (fornitore)
        references Fornitore(partitaIVA),
    foreign key (dipartimento)
        references Dipartimento(nome)
);




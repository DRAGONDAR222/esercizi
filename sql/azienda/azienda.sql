-- CREATE DATABASE azienda;

-- \c azienda

CREATE DOMAIN Stringa AS varchar;

CREATE DOMAIN IntGZ AS integer
    CHECK (VALUE > 0);

CREATE DOMAIN CodiceFiscale AS char(16);

CREATE TYPE Indirizzo AS (
    via Stringa,
    civico Stringa,
    CAP integer
);

CREATE TYPE Denaro AS (
    valore IntGZ,
    valuta Stringa 
);


CREATE TABLE Dipartimento (
    id integer primary key,
    nome Stringa not null,
    telefono Stringa not null
);

CREATE TABLE Impiegato (
    id integer primary key,
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita date not null,
    stipendio Denaro not null,
    dipartimento integer,
    foreign key (dipartimento)
        references Dipartimento(id)
);

CREATE TABLE Afferenza (
    impiegato_id integer not null,
    dipartimento_id integer not null,
    data_afferenza date not null,
    primary key (impiegato_id, dipartimento_id, data_afferenza),
    foreign key (impiegato_id)
        references Impiegato(id),
    foreign key (dipartimento_id)
        references Dipartimento(id)
);

CREATE TABLE Proggetto (
    id integer primary key,
    nome Stringa not null,
    budget Denaro not null
);

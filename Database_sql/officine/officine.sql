-- create database officine;

-- \c officine

CREATE DOMAIN Stringa AS varchar(255);

CREATE DOMAIN CodiceFiscale AS char(16);

CREATE DOMAIN posinteger AS integer
CHECK (value >= 0);

CREATE TYPE Indirizzo AS (
    via Stringa,
    civico Stringa,
    CAP integer
);

CREATE DOMAIN Targa AS varchar(10)
CHECK (VALUE ~ '^[A-Z]{2}[0-9]{3}[A-Z]{2}$');

CREATE DOMAIN Telefono AS varchar(20)
CHECK (value ~ '^\+?[0-9\s\-\(\)]{6,20}$');

CREATE TABLE Proprietario(
    id integer PRIMARY KEY
);

CREATE TABLE Direttore(
    id integer PRIMARY KEY,
    data_nascita date NOT NULL
);

CREATE TABLE Officina(
    id integer PRIMARY KEY,
    nome Stringa NOT NULL,
    indirizzo Indirizzo NOT NULL,
    n_dipendenti posinteger NOT NULL,
    direttore integer UNIQUE NOT NULL,
    FOREIGN KEY(direttore) REFERENCES Direttore(id)
);

CREATE TABLE Dipendente(
    id integer PRIMARY KEY,
    anni_servizio integer NOT NULL,
    officina integer NOT NULL,
    FOREIGN KEY(officina) REFERENCES Officina(id)
);

CREATE TABLE Persona(
    id integer PRIMARY KEY,
    nome Stringa NOT NULL,
    cf CodiceFiscale NOT NULL UNIQUE,
    indirizzo Indirizzo NOT NULL,
    cell Telefono NOT NULL,
    proprietario integer UNIQUE,
    direttore integer UNIQUE,
    dipendente integer UNIQUE,
    FOREIGN KEY(proprietario) REFERENCES Proprietario(id),
    FOREIGN KEY(direttore) REFERENCES Direttore(id),
    FOREIGN KEY(dipendente) REFERENCES Dipendente(id)
);

CREATE TABLE Veicolo(
    modello Stringa NOT NULL,
    tipo Stringa NOT NULL,
    targa Targa PRIMARY KEY,
    anno_I integer NOT NULL,
    proprietario integer NOT NULL,
    FOREIGN KEY(proprietario) REFERENCES Proprietario(id)
);

CREATE TABLE In_corso(
    id integer PRIMARY KEY
);

CREATE TABLE Terminata(
    id integer PRIMARY KEY,
    data_c date NOT NULL,
    ora_c integer NOT NULL
);

CREATE TABLE Riparazione(
    codice Stringa NOT NULL,
    data_A date NOT NULL,
    ora_A integer NOT NULL,
    id integer PRIMARY KEY,
    in_corso integer UNIQUE,
    terminata integer UNIQUE,
    veicolo Targa NOT NULL,
    FOREIGN KEY(terminata) REFERENCES Terminata(id),
    FOREIGN KEY(in_corso) REFERENCES In_corso(id),
    FOREIGN KEY(veicolo) REFERENCES Veicolo(targa)
);
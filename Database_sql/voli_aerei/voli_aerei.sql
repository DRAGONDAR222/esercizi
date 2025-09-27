-- CREATE DATABASE voli_aerei

-- \c voli_aerei

CREATE DOMAIN IntGEZ AS integer
    CHECK (VALUE >= 0);

CREATE DOMAIN IntGZ1900 AS integer
    CHECK (VALUE > 1900);

CREATE DOMAIN Stringa AS varchar;

CREATE DOMAIN IntGZ AS integer
    CHECK (VALUE > 0);


CREATE TABLE Nazione(
    nome Stringa not null,
    id integer primary key
);

CREATE TABLE Citta(
    nome Stringa not null,
    n_abitanti IntGEZ not null,
    nazione integer not null,
    id integer primary key,
    FOREIGN KEY (nazione)
        REFERENCES Nazione(id)
);

CREATE TABLE CompagniaAerea(
    nome Stringa not null,
    fondazione IntGZ1900 not null,
    citta integer not null,
    id integer primary key,
    FOREIGN Key (citta)
        REFERENCES Citta(id)
);

CREATE TABLE Aeroporto(
    codice Stringa not null,
    nome Stringa not null,
    citta integer not null,
    id integer primary key,
    FOREIGN Key (citta)
        REFERENCES Citta(id)
);


CREATE TABLE Volo(
    codice Stringa not null,
    durata IntGZ not null,
    id Integer primary key,
    compagniaAerea integer not null,
    aeroporto_arrivo integer not null,
    aeroporto_partenza integer not null,
    FOREIGN KEY (compagniaAerea)
        REFERENCES CompagniaAerea(id),
    FOREIGN KEY (aeroporto_arrivo)
        REFERENCES Aeroporto(id),
    FOREIGN KEY (aeroporto_partenza)
        REFERENCES Aeroporto(id)
);
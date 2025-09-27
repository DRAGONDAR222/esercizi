-- CREATE DATABASE accademia;

-- \c accademia

CREATE TYPE Strutturato AS ENUM
    ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

CREATE TYPE LavoroProgetto AS ENUM
    ('Ricerca e Sviluppo', 'Dimostrazione', 'Managment', 'Altro');

CREATE TYPE LavoroNonProgettuale AS ENUM
    ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

CREATE TYPE CausaAssenza AS ENUM
    ('Chiusura Universitaria', 'Maternità', 'Malattia');

CREATE DOMAIN Posinteger AS integer
    CHECK (VALUE >= 0);

CREATE DOMAIN StringaM AS varchar(100);

CREATE DOMAIN Denaro AS numeric(10,2)
    CHECK (VALUE >= 0);

CREATE DOMAIN NumeroOre AS integer
    CHECK (VALUE > 0 AND VALUE <= 8);

CREATE TABLE Persona (
    id Posinteger PRIMARY KEY,
    nome StringaM NOT NULL,
    cognome StringaM NOT NULL,
    posizione Strutturato NOT NULL,
    stipendio Denaro NOT NULL
);

CREATE TABLE Progetto (
    id Posinteger PRIMARY KEY,
    nome StringaM NOT NULL,
    UNIQUE (id, nome),
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    budget Denaro,
    CHECK (inizio < fine)
);

CREATE TABLE WP (
    progetto Posinteger NOT NULL,
    id Posinteger NOT NULL,
    PRIMARY KEY (progetto, id),
    nome StringaM,
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    UNIQUE (progetto, nome),
    FOREIGN KEY (progetto) REFERENCES Progetto(id),
    CHECK (inizio < fine)
);

CREATE TABLE AttivitàProgetto (
    id Posinteger PRIMARY KEY,
    persona Posinteger NOT NULL,
    progetto Posinteger NOT NULL,
    wp Posinteger NOT NULL,
    giorno DATE NOT NULL,
    tipo LavoroProgetto NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id),
    FOREIGN KEY (progetto, wp) REFERENCES WP(progetto, id)
);

CREATE TABLE AttivitàNonProgettuale (
    id Posinteger PRIMARY KEY,
    persona Posinteger NOT NULL,
    tipo LavoroNonProgettuale NOT NULL,
    giorno DATE NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id)
);

CREATE TABLE Assenza (
    id Posinteger PRIMARY KEY,
    persona Posinteger NOT NULL,
    tipo CausaAssenza NOT NULL,
    giorno DATE NOT NULL,
    UNIQUE (persona, giorno),
    FOREIGN KEY (persona) REFERENCES Persona(id)
);

CREATE DOMAIN Stringa AS varchar(255);

CREATE DOMAIN CodiceFiscale AS char(16);

CREATE DOMAIN posinteger AS integer CHECK (VALUE >= 0);

CREATE DOMAIN Targa AS varchar(10) CHECK (VALUE ~ '^[A-Z]{2}[0-9]{3}[A-Z]{2}$');

CREATE DOMAIN Telefono AS varchar(20) CHECK (VALUE ~ '^\+?[0-9\s\-\(\)]{6,20}$');

CREATE TYPE Indirizzo AS (
    via Stringa,
    civico Stringa,
    CAP integer
);


CREATE TABLE Proprietario(
    id SERIAL PRIMARY KEY
);

CREATE TABLE Direttore(
    id SERIAL PRIMARY KEY,
    data_nascita date NOT NULL
);

CREATE TABLE Officina(
    id SERIAL PRIMARY KEY,
    nome Stringa NOT NULL,
    indirizzo Indirizzo NOT NULL,
    n_dipendenti posinteger NOT NULL,
    direttore integer NOT NULL,
    FOREIGN KEY(direttore) REFERENCES Direttore(id)
);

CREATE TABLE Dipendente(
    id SERIAL PRIMARY KEY,
    anni_servizio integer NOT NULL,
    officina integer NOT NULL,
    FOREIGN KEY(officina) REFERENCES Officina(id)
);

CREATE TABLE Persona(
    id SERIAL PRIMARY KEY,
    nome Stringa NOT NULL,
    cf CodiceFiscale NOT NULL,
    indirizzo Indirizzo NOT NULL,
    cell Telefono NOT NULL,
    proprietario integer,
    direttore integer,
    dipendente integer,
    FOREIGN KEY(proprietario) REFERENCES Proprietario(id),
    FOREIGN KEY(direttore) REFERENCES Direttore(id),
    FOREIGN KEY(dipendente) REFERENCES Dipendente(id)
);

CREATE TABLE Veicolo(
    targa Targa PRIMARY KEY,
    modello Stringa NOT NULL,
    tipo Stringa NOT NULL,
    anno_I integer NOT NULL,
    proprietario integer NOT NULL,
    FOREIGN KEY(proprietario) REFERENCES Proprietario(id)
);

CREATE TABLE In_corso(
    id SERIAL PRIMARY KEY
);

CREATE TABLE Terminata(
    id SERIAL PRIMARY KEY,
    data_c date NOT NULL,
    ora_c integer NOT NULL
);

CREATE TABLE Riparazione(
    id SERIAL NOT NULL,
    veicolo Targa NOT NULL,
    codice Stringa NOT NULL,
    data_A date NOT NULL,
    ora_A integer NOT NULL,
    in_corso integer,
    terminata integer,
    PRIMARY KEY(id, veicolo),
    FOREIGN KEY(in_corso) REFERENCES In_corso(id),
    FOREIGN KEY(terminata) REFERENCES Terminata(id),
    FOREIGN KEY(veicolo) REFERENCES Veicolo(targa)
);

-- create database accademia;

-- \c accademia


create type Strutturato as enum
('Ricercatore','Professore Associato','Professore Ordinario');

create type LavoroProgetto as enum
('Ricerca e Sviluppo','Dimostrazione','Managment','Altro');

create type LavoroNonProgettuale as enum
('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro
Accademico', 'Altro');

create type CausaAssenza as enum
('Chiusura Univerisataria','Maternità','Malattia');

create domain Posinteger as integer
    check (value > 0);

create domain StringaM as varchar(100);

create domain NumeroOre as Posinteger
    check (value < 8);

create domain Denaro as integer
    check (value >= 0);


create table Persona(
    id Posinteger primary key,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null
);

create table Progetto(
    id Posinteger primary key,
    nome StringaM not null,
    unique ( id, nome),
    inizio date not null,
    fine date not null,
    budget Denaro,
    check (inizio < fine)
);

create table WP(
    progetto Posinteger not null,
    id Posinteger not null,
    primary key(progetto,id),
    nome StringaM,
    inizio date not null,
    fine date not null,
    unique (progetto, nome),
    foreign key (progetto)
        references Progetto(id),
    check (inizio < fine)
);

create table AttivitàProgetto(
    id Posinteger primary key,
    persona Posinteger not null,
    progetto Posinteger not null,
    wp Posinteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    foreign key (persona)
        references Persona(id),
    foreign key (progetto,wp)
        references WP(progetto,id)
);

create table AttivitàNonProgettuale(
    id Posinteger primary key,
    persona Posinteger not null,
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null,
    foreign key (persona)
        references Persona(id)
);

create table Assenza(
    id Posinteger primary key,
    persona Posinteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    unique (persona, giorno),
    foreign key (persona)
        references Persona(id)
);

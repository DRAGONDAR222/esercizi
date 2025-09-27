-- CREATE DATABASE Impiegati_e_Studenti;

-- \c impiegati_e_studenti

create domain stringa as varchar(255);

create domain intgez as integer
	check (value >= 0);

create domain realgez as real
	check (value >= 0);

create type ruolo as enum
	('Direttore', 'Segretario', 'Progettista');

create domain codicefiscale as char(16)
	check (value ~ '^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$');

create table posizionemilitare(
	nome stringa primary key
);

create table persona(
	cf codicefiscale primary key,
	nome stringa not null,
	cognome stringa not null,
	data_nascita date not null,
	maternita intgez,
	is_uomo boolean not null,
	is_donna boolean not null,
	pos_uomo stringa,
	foreign key (pos_uomo)
		references posizionemilitare(nome),

	-- vincoli di ennupla per implementare 
	--  [V.Persona.Genere.complete]
	check (
		(is_uomo = true)
		=
		(pos_uomo is not null)
		),
		-- o, equivalentemente ma è più lungo)
		-- (is_uomo = true and pos_uomo is not null)
		-- OR
		-- (is_uomo = false and pos_uomo is null)
	check (
		(is_donna = true)
		=
		(maternita is not null)),
	check (is_uomo = true or is_donna = true)
);

create table studente (
	persona codicefiscale primary key,
	foreign key (persona) 
		references persona(cf),
	matricola intgez not null,
	unique(matricola)
);

create table impiegato (
	persona codicefiscale primary key,
	foreign key (persona) 
		references persona(cf),
	stipendio realgez not null,
	ruolo ruolo not null
);

create table progetto (
	id serial primary key,
	nome stringa not null,

	resp_prog codicefiscale not null,
	foreign key (resp_prog)
		references impiegato(persona)
);

-- Vincoli non implementabili direttamente
-- 	nello schema relazionale:

-- [V.Impiegato.Progettista.responsabile]
--	Per ogni i:Impiegato
--	 se i è coinvolto in un link resp_prog
--	 allora i.ruolo = 'Progettista'

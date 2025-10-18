begin transaction;

set constraints all deferred;

CREATE DOMAIN Stringa as varchar;

CREATE DOMAIN IntGZ as integer
	check (value > 0);

CREATE DOMAIN Real_0_10 as real
	check (value >= 0 and value <= 8);

CREATE TYPE regole as ENUM 
('Giapponesi', 'Cinesi');

CREATE TYPE colore as ENUM 
('Bianco', 'Nero');

CREATE TYPE indirizzo as (
	via Stringa,
	civico Stringa
);

create table nazione (
	nome stringa primary key
);

create table regione (
	nome stringa not null,

	-- accorpa l'associazione reg_naz
	nazione stringa not null,
	primary key (nome, nazione),

	foreign key (nazione) references nazione(nome)
);

create table citta (
	-- creo un id artificiale che renda più comodo definire le FK verso questa tabella
	id integer primary key, 
	nome stringa not null,
	regione stringa not null,
	nazione stringa not null,

	unique (nome, regione, nazione),

	foreign key (regione, nazione)
		references regione(nome, nazione)
);

create table giocatore (
	nickname stringa primary key,
	nome stringa not null,
	cognome stringa not null,
	indirizzo indirizzo not null,
	rank IntGZ not null,

	-- accorpo l'associazione cit_gioc
	citta integer not null,
	foreign key (citta) references citta(id)

	-- alternativa, "più pesante" perché devo portarmi dietro tutta la chiave primaria di citta
	-- citta stringa not null,
	-- regione stringa not null,
	-- nazione stringa not null,
	-- foreign key (citta, regione, nazione)
		-- references citta(nome, regione, nazione)
);


create table torneo (
	id integer primary key,
	nome stringa not null,
	descrizione stringa not null,
	anno_edizione integer not null
);

create table partita (
	id integer primary key,
	data date not null,
	regole regole not null,
	indirizzo indirizzo not null,
	komi Real_0_10 not null,

	-- accorpo l'associazione bianco
	bianco stringa not null,
	foreign key (bianco)
		references giocatore(nickname),

	-- non accorpo l'associazione nero

	torneo integer, -- può essere null, è [0..1]
	foreign key (torneo)
		references torneo(id),

	-- accorpa part_cit
	citta integer not null,
	foreign key (citta) references citta(id)
);

create table nero (
	giocatore stringa not null,
	partita integer not null,
	primary key (partita), -- una partita ha un solo giocatore nero
	foreign key (giocatore)
		references giocatore(nickname),
	foreign key (partita)
		references partita (id) deferrable

);

alter table partita add constraint partita_nero_fk
	-- v. incl. id appare in nero(partita) --> ma partita è chiave nella tabella nero! --> diventa una FK
	foreign key (id) references nero(partita) deferrable;

create table PartitaConPunteggi (
	-- devo necessariamente accorpare punt_isa_part perché ospita l'identificatore primario
	partita integer primary key,

	foreign key (partita) references partita(id),
	punteggio_bianco IntGZ not null,
	punteggio_nero IntGZ not null
);

create table PartitaConRinuncia (
	-- devo necessariamente accorpare rin_isa_part perché ospita l'identificatore primario
	partita integer primary key,

	foreign key (partita) references partita(id),
	rinunciatario colore not null
);

commit;


INSERT INTO giocatore (...) VALUES ('Marcelxxx', ...);
begin transaction;

set constraints all deferred;


insert into partita(id, bianco, nero, ...) value (1, ...)
insert into nero(partita, giocatore) values (1, 'Marcelxxx');

commit;
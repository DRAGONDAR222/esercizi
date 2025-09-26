-- CREATE DATABASE e_buy;


create table categoria (
	nome stringa primary key,
	-- tutti gli altri attributi di categoria
	super stringa,
	check (nome <> super)
);

alter table categoria add 
	foreign key (super) 
		references categoria(nome);


create table utente (
	username stringa primary key,
	registrazione timestamp not null
);

create table privato (
	utente stringa primary key,
	foreign key (utente)
		references utente(username) deferrable
);

create table venditoreprof (
	utente stringa primary key,
	vetrina URL not null,
	unique (vetrina),
	foreign key (utente)
		references utente(username) deferrable
);

-- Vincoli {disjoint, complete} su Utente non ancora implementati

create table metodopagamento (
	nome stringa primary key
);

create table postoggetto(
	id serial primary key,
	pubblica stringa not null,  -- l'utente che pubblica
	unique(id, pubblica), -- chiave non-minimale
	descrizione stringa not null,
	pubblicazione timestamp not null,
	ha_feedback boolean not null default false,
	voto Voto,
	commento stringa,
	istante_feedback timestamp,
	categoria stringa not null,
	
	foreign key (pubblica)
		references utente(username),

	-- superfluo, ma lo scriviamo lo stesso perché può essere implementato come vincolo di ennupla
	check (istante_feedback is null or istante_feedback > pubblicazione), 
	check (
		(ha_feedback = true)
		=
		(voto is not null and istante_feedback is not null)
	),
	check ( commento is not null or ha_feedback = true), -- ho usato A -> B == (NOT A) OR B

	
	foreign key (categoria)
		references categoria(nome)

	-- v.incl. (id) occorre in met_post(postoggetto)
);


create table met_post(
	postoggetto integer not null,
	metodo stringa not null,
	primary key (postoggetto, metodo),
	foreign key (postoggetto)
		references postoggetto(id),
	foreign key (metodo)
		references metodopagamento(nome)
);

create table postoggettousato(
	postoggetto integer primary key,
	foreign key (postoggetto)
		references postoggetto(id) deferrable,
	condizione condizione not null,
	anni_garanzia intgez not null
);

create table postoggettonuovo(
	postoggetto integer primary key,
	foreign key (postoggetto)
		references postoggetto(id) deferrable,
	anni_garanzia intge2 not null,
	pubblica_nuovo stringa not null,
	foreign key (pubblica_nuovo)
		references venditoreprof(utente) deferrable,

	foreign key (postoggetto, pubblica_nuovo)
		references postoggetto(id, pubblica) deferrable
);

-- Vincoli {disjoint, complete} su PostOggetto nuovo/usato non ancora implementati

create table postoggettocompralosubito(
	postoggetto integer primary key,
	foreign key (postoggetto)
		references postoggetto(id) deferrable,
	prezzo realgz not null,
	acquirente stringa,
	foreign key (acquirente)
		references privato(utente),
	istante_acquisto timestamp,
	check( 
		(acquirente is null) = (istante_acquisto is null)
	)
);

create table postoggettoasta(
	postoggetto integer primary key,
	foreign key (postoggetto)
		references postoggetto(id) deferrable,
	prezzo_base realgez not null,
	prezzo_bid realgz not null,
	scadenza timestamp not null
);

create table bid(
	codice serial primary key,
	istante timestamp not null,
	asta_bid integer not null,
	foreign key (asta_bid)
		references postoggettoasta(postoggetto),
	unique(istante, asta_bid),
	bid_ut stringa not null,
	foreign key (bid_ut)
		references privato(utente)
);









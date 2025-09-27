-- DOMAIN --

CREATE DOMAIN stringa AS varchar (255);
CREATE DOMAIN URL AS varchar (2048);
CREATE DOMAIN IntG1 AS integer
    check (value > 1 );
CREATE DOMAIN IntGEZ AS integer
    check (value >= 0 );
CREATE DOMAIN RealGZ AS Real
    check (value > 0 );
CREATE DOMAIN RealGEZ AS Real
    check (value >= 0 );
CREATE DOMAIN Voto AS integer
    check (value >= 1 and value <= 5);

CREATE TYPE Condizione AS ENUM
    ('Ottimo', 'Buono', 'Discreto', 'Da sistemare');


-- TABLE --

CREATE TABLE Categoria(
    nome stringa primary key,
    super stringa
);
-- Perche la foreign key si riferisce a se stessa ma ancora non esiste
alter table categoria 
add constraint fk_categoria_super
foreign key (super) references categoria(nome);


CREATE TABLE Utente(
    username stringa primary key,
    registrazione timestamp not null
);


CREATE TABLE PostOggetto(
    descrizione stringa not null,
    pubblicazione timestamp not null,
    ha_feedback boolean not null,
    voto Voto,
    commento stringa,
    istante_feedback timestamp,
    id serial primary key,
    pubblica stringa not null ,
    foreign key (pubblica)
        references Utente(username),

    check(
            (
                (
                    (ha_feedback = true)
                    =
                    (voto is not null and istante_feedback is not null))                    
                )
            check
                (
                    not(
                    (ha_feedback = true)
                    =
                    (voto is not null and istante_feedback is not null))
                    )
                    and
                    not(commento is not null)
                )
            )
        
);

CREATE TABLE MetodiDiPagamento(
    nome stringa primary key
);

CREATE TABLE PostOggettoUsato(
    pou_isa_po integer primary key,
    foreign key (pou_isa_po)
        references PostOggetto(id),
    condizione Condizione not null,
    anni_garanzia IntGEZ not null
);

CREATE TABLE VenditoreProfessionale(
    vetrina URL not null,
    unique(vetrina),
    vp_isa_ut stringa primary key,
    foreign key (vp_isa_ut)
        references Utente(username)
);

CREATE TABLE PostOggettoNuovo(
    pon_isa_po integer primary key,
    foreign key (pon_isa_po)
        references PostOggetto(id),
    anni_garanzia IntG1 not null,
    pubblica_nuovo stringa not null,
    foreign key (pubblica_nuovo)
        references VenditoreProfessionale (vp_isa_ut)
    );

CREATE TABLE Privato(
    pr_isa_ut stringa primary key,
    foreign key (pr_isa_ut)
        references Utente(username)
);

CREATE TABLE Asta(
    asta_isa_po integer primary key,
    foreign key (asta_isa_po)
        references PostOggetto(id),
    prezzo_base RealGEZ not null,
    prezzo_bid RealGZ not null,
    scadenza timestamp not null
);

CREATE TABLE Bid(
    codice serial primary key,
    istante timestamp not null,
    asta_bid integer not null,
    unique (istante, asta_bid),
    foreign key (asta_bid)
        references Asta (asta_isa_po)
);

CREATE TABLE CompraloSubito(
    cs_isa_po integer primary key,
    foreign key (cs_isa_po)
        references PostOggetto(id),
    prezzo RealGZ not null,
    istante_acquirente timestamp,

    check
);
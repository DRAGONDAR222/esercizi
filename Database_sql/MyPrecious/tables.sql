create table Nazione(
    id serial primary key
);

create table Regione(
    id serial not null,
    nazione integer not null,
    foreign key(nazione) references nazione(id)
);

create table Citta(
    id serial not null,
    regione integer not null,
    foreign key(regione) references regione(id)
);

create table Opera(
    id serial primary key,
    nome stringa not null,
    anno_realizzazione integer not null
);

create table Artista(
    id serial primary key,
    nome_arte stringa not null,
    data_nascita date not null,
    data_morte date,
    op_art integer,
    foreign key(op_art) references opera(id)
);

create table Tecnica(
    id serial primary key,
    nome stringa not null,
    op_tec integer,
    foreign key(op_tec) references opera(id)
);

create table Categoria(
    nome stringa not null,
    op_cat integer not null,
    primary key(op_cat, nome),
    foreign key(op_cat) references opera(id)
);

create table Correnteartistica(
    nome stringa not null,
    op_corr integer not null,
    primary key(op_corr, nome),
    foreign key(op_corr) references opera(id)
);

create table Tariffa(
    nome stringa primary key
);

create table Biglietto(
    id serial primary key,
    istante_vendita timestamp not null,
    validita date not null
);

create table Standard(
    id serial not null,
    big_isa_stan integer not null,
    primary key(id, big_isa_stan),
    foreign key(big_isa_stan) references biglietto(id)
);

create table Extendedaccess(
    id serial not null,
    big_isa_text integer not null,
    primary key(id, big_isa_text),
    foreign key(big_isa_text) references biglietto(id)
);

create table Esposizione(
    id serial not null,
    nome stringa not null,
    inizio date not null,
    primary key(id)
);

create table Temporanea(
    id serial not null,
    esp_isa_perm integer not null,
    fine date not null,
    tema stringa not null,
    prezzo_accesso real not null check(prezzo_accesso >= 0),
    primary key(id),
    foreign key(esp_isa_perm) references esposizione(id)
);

create table Permanente(
    id serial not null,
    esp_isa_temp integer not null,
    primary key(id, esp_isa_temp),
    foreign key(esp_isa_temp) references esposizione(id)
);

create table Espone(
    opera integer not null,
    esposizione integer not null,
    inizio date not null,
    fine date,
    primary key(opera, esposizione),
    foreign key(opera) references opera(id),
    foreign key(esposizione) references esposizione(id)
);

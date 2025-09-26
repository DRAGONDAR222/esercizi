-- categorie

insert into categoria(nome, super)
values
('Elettronica', NULL),
('Informatica', 'Elettronica'),
('Laptop', 'Informatica'),
('Casa e giardino', NULL),
('Arredamento', 'Casa e giardino'),
('Giardinaggio', 'Casa e giardino');

begin transaction;
	set constraints all deferred;
insert into utente(username, registrazione)
values
('U99001', current_timestamp),
('U99002', current_timestamp),
('U99003', current_timestamp),
('U99004', current_timestamp);


insert into privato(utente)
values
('U99001'),
('U99002');


insert into venditoreprof(utente, vetrina)
values
('U99003', 'http://www.example.u3.com'),
('U99004', 'http://www.example.u4.com');

commit;
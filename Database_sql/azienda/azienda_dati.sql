-- Inserimento Dipartimento
INSERT INTO Dipartimento (id, nome, telefono) VALUES
(1, 'Amministrazione', '0612345678'),
(2, 'Finanza', '0623456789'),
(3, 'Marketing', '0634567890'),
(4, 'IT', '0645678901'),
(5, 'Risorse Umane', '0656789012'),
(6, 'Logistica', '0667890123'),
(7, 'Vendite', '0678901234'),
(8, 'Produzione', '0689012345'),
(9, 'Ricerca e Sviluppo', '0690123456'),
(10, 'Servizi Generali', '0601234567');

-- Inserimento Impiegato
INSERT INTO Impiegato (id, nome, cognome, data_nascita, stipendio, dipartimento) VALUES
(1, 'Mario', 'Rossi', '1985-03-15', ROW(3200, 'EUR'), 1),
(2, 'Lucia', 'Bianchi', '1990-07-22', ROW(2900, 'EUR'), 2),
(3, 'Giovanni', 'Verdi', '1982-11-01', ROW(3500, 'EUR'), 3),
(4, 'Anna', 'Neri', '1995-01-10', ROW(2800, 'EUR'), 4),
(5, 'Paolo', 'Russo', '1988-09-18', ROW(3000, 'EUR'), 5),
(6, 'Sara', 'Conti', '1993-06-25', ROW(2700, 'EUR'), 6),
(7, 'Marco', 'Ferrari', '1986-02-14', ROW(3100, 'EUR'), 7),
(8, 'Elisa', 'Romano', '1991-08-30', ROW(2950, 'EUR'), 8),
(9, 'Luca', 'De Luca', '1987-12-19', ROW(3300, 'EUR'), 9),
(10, 'Chiara', 'Costa', '1994-05-04', ROW(2850, 'EUR'), 10),
(11, 'Davide', 'Moretti', '1980-03-08', ROW(3700, 'EUR'), 1),
(12, 'Francesca', 'Fontana', '1992-10-20', ROW(3100, 'EUR'), 2),
(13, 'Stefano', 'Galli', '1983-06-12', ROW(3450, 'EUR'), 3),
(14, 'Laura', 'Grassi', '1996-11-25', ROW(2600, 'EUR'), 4),
(15, 'Alessandro', 'Marini', '1989-01-30', ROW(3150, 'EUR'), 5);

-- Inserimento Afferenza
INSERT INTO Afferenza (impiegato_id, dipartimento_id, data_afferenza) VALUES
(1, 1, '2020-01-01'),
(2, 2, '2021-03-15'),
(3, 3, '2019-06-10'),
(4, 4, '2022-02-05'),
(5, 5, '2021-07-07'),
(6, 6, '2022-09-12'),
(7, 7, '2020-10-10'),
(8, 8, '2023-01-20'),
(9, 9, '2018-11-11'),
(10, 10, '2019-04-04'),
(11, 1, '2018-05-15'),
(12, 2, '2020-06-30'),
(13, 3, '2017-09-19'),
(14, 4, '2021-12-12'),
(15, 5, '2023-03-01');

-- Inserimento Proggetto
INSERT INTO Proggetto (id, nome, budget) VALUES
(1, 'Sistema ERP', ROW(50000, 'EUR')),
(2, 'Campagna Pubblicitaria', ROW(30000, 'EUR')),
(3, 'Analisi Mercato', ROW(20000, 'EUR')),
(4, 'Migrazione Cloud', ROW(45000, 'EUR')),
(5, 'Recruiting HR 2025', ROW(15000, 'EUR')),
(6, 'Espansione Sede Milano', ROW(80000, 'EUR')),
(7, 'Automazione Magazzino', ROW(60000, 'EUR')),
(8, 'CRM Clienti 2.0', ROW(25000, 'EUR')),
(9, 'Formazione Dipendenti', ROW(10000, 'EUR')),
(10, 'Progetto Sostenibilità', ROW(40000, 'EUR'));

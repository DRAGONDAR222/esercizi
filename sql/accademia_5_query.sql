-- 1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
-- ‘Pegasus’ ?

select WP.nome, WP.inizio, WP.fine
from Progetto, WP
where Progetto.nome = 'Pegasus' 
  and Progetto.id = WP.progetto;

--2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
-- una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

select distinct p.nome, p.cognome, p.posizione
from Persona as p, AttivitàProgetto as ap, Progetto as pr
where p.id = ap.persona and ap.progetto = pr.id and pr.nome ='Pegasus'
order by p.cognome desc;

-- 3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
-- una attività nel progetto ‘Pegasus’ ?

select distinct p.nome, p.cognome, p.posizione
from Persona as p, AttivitàProgetto as ap, AttivitàProgetto as ap2, Progetto as pr
where p.id = ap.persona and ap.progetto = pr.id and pr.nome ='Pegasus'
and ap2.id <> ap.id and ap2.persona = ap.persona
and ap2.progetto = ap.progetto
order by p.cognome desc;

-- 4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto almeno una assenza per malattia?


select distinct p.nome, p.cognome 
from Persona p, Assenza a
where p.posizione = 'Professore Ordinario' 
and a.persona = p.id 
and a.tipo = 'Malattia'

-- 5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto più di una assenza per malattia?

select distinct p.nome, p.cognome 
from Persona p, Assenza a, Assenza a1
where p.posizione = 'Professore Ordinario' and a.persona = p.id and a.tipo = 'Malattia'
and a.id <> a1.id
and a.persona = a1.persona

-- 6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
-- un impegno per didattica?

select distinct p.nome, p.cognome 
from Persona p, AttivitàNonProgettuale a
where p.posizione = 'Ricercatore' and a.persona = p.id and a.tipo = 'Didattica'

-- 7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
-- impegno per didattica?

select distinct p.nome, p.cognome 
from Persona p, AttivitàNonProgettuale a, AttivitàNonProgettuale a1
where p.posizione = 'Ricercatore' and a.persona = p.id and a.tipo = 'Didattica'
and a.id <> a1.id
and a.persona = a1.persona

-- 8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali?

select distinct p.nome, p.cognome 
from Persona p, AttivitàNonProgettuale an, AttivitàProgetto a
where an.giorno = a.giorno
and a.persona = p.id 
and an.persona = p.id

-- 9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali? Si richiede anche di proiettare il
-- giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
-- entrambe le attività.

select distinct p.nome, p.cognome, a.giorno, pr.nome, an.tipo, an.oreDurata, a.oreDurata
from Persona p, AttivitàNonProgettuale an, AttivitàProgetto a, Progetto pr
where an.giorno = a.giorno
and a.persona = p.id 
and an.persona = p.id
and a.progetto = pr.id;


-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?

select distinct p.nome, p.cognome 
from Persona p, Assenza ass, AttivitàProgetto a
where ass.giorno = a.giorno
and a.persona = p.id 
and ass.persona = p.id

-- 11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
-- nome del progetto, la causa di assenza e la durata in ore della attività progettuale.

select distinct p.nome, p.cognome, a.oreDurata, ass.giorno, pr.nome, ass.tipo
from Persona p, Assenza ass, AttivitàProgetto a, Progetto pr
where ass.giorno = a.giorno
and a.persona = p.id 
and ass.persona = p.id
and a.progetto = pr.id


-- 1 2 ) Q u a l i s o n o i WP c he hanno l o s t e s s o nome , ma a p p a r t e n g o n o
-- a p r o g e t t i d i v e r s i ?

select wp1.nome, wp1.progetto AS progetto1, wp2.progetto AS progetto2
from WP wp1, WP wp2
where wp1.nome = wp2.nome 
  and wp1.progetto < wp2.progetto
  and wp1.nome is not null;



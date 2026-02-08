-- Scrivere una query SQL che trovi il nome e il cognome dei docenti 
-- (professori ordinari e associati) che hanno lavorato su tutti i progetti 
-- presenti nel database.


select p.id, p.nome, p.cognome
from Persona p
join AttivitàProgetto ap
  on ap.persona = p.id
join Progetto prog
  on prog.id = ap.progetto
where p.posizione in ('Professore Associato', 'Professore Ordinario')
group by p.id, p.nome, p.cognome
having count(distinct ap.progetto) = 
       (select count(*) from Progetto);

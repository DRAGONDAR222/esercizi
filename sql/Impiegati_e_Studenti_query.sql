-- Quali sono i nomi degli impiegati nati a partire dall'anno 

select p.nome, p.cognome
from persona p, impiegato i
where i.persona = p.cf
order by p.data_nascita asc

-- Quali sono i nomi di tutti i progetti?

select distinct prog.nome
from progetto prog

-- Quali sono gli stipendi dei direttori?

select distinct i.stipendio
from impiegato i
where i.ruolo = 'Direttore'

-- Quanti sono i progettisti?

select count(*) 
from impiegato i
where i.ruolo = 'Progettista'

-- Quanti sono i responsabili?

select distinct count(*) 
from impiegato i, progetto prog
where i.ruolo = 'Progettista'
and prog.resp_prog = i.persona

-- Quanti sono i progettisti che non sono responsabili? 

select count(*)
from impiegato
where ruolo = 'Proggettista'
and personanot not in (select distinct resp_prog from progetto)


-- Qual è lo stipendio medio dei segretari?

select avg(i.stipendio) 
from impiegato i
where i.ruolo = 'Segretario'

-- Qual è l'età della/o studente meno giovane?

select date_part('year' , age(current_date, min(p.data_nascita))) 
from studente stud, persona p
where stud.persona = p.cf

-- Quanti sono i direttori che hanno assolto agli obblighi militari?

select p.nome
from impiegato i, persona p
where p.pos_uomo = 'Assolto'
and p.cf = i.persona
and i.ruolo = 'Direttore'

-- Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?

select count(prog.id)
from impiegato i, persona p, progetto prog
where prog.resp_prog = i.persona
and p.cf = i.persona
and i.ruolo = 'Progettista'
and p.maternita => 2

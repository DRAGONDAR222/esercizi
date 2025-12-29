-- 1. Quali sono le persone con stipendio di al massimo 40000
-- euro [2 punti]

select *
from persona p
where p.stipendio < 40000

-- 2. Quali sono i ricercatori che lavorano ad almeno un
-- progetto e hanno uno stipendio di al massimo 40000 [2
-- punti]

select *
from persona p
where p.stipendio < 40000
    and p.posizione = 'Ricercatore'


-- corretta
select distinct p.id,p.nome,p.cognome
from persona p
    join AttivitàProgetto ap
    on p.id = ap.persona
where p.stiperndio <= 40000
    and posizione = 'Ricercatore'

-- 3. Qual è il budget totale dei progetti nel db [2 punti]

select sum(prog.budget)
from progetto prog

-- corretta
selct sum(budget)
from progetto prog

-- 4. Qual è il budget totale dei progetti a cui lavora ogni
-- persona. Per ogni persona restituire nome, cognome e
-- budget totale dei progetti nei quali è coinvolto. [3 punti]

select p.nome, p.cognome, sum(distinct prog.budget)
from progetto prog
join AttivitàProgetto ap
    on ap.progetto = prog.id
join persona p
    on p.id = ap.id
group by p.id, p.nome

--corretta
select p.id, p.nome, p.congome, sum(pr.budget)
from persona p, progetto pr, AttivitàProgetto accademia
where 
    p.id = a.persona
    and a.progetto = pr.id
group by p.id

-- 5. Qual è il numero di progetti a cui partecipa ogni
-- professore ordinario. Per ogni professore ordinario,
-- restituire nome, cognome, numero di progetti nei quali è
-- coinvolto [3 punti]

select p.id, p.nome, p.cognome, count(distinct prog.id)
from progetto prog
join AttivitàProgetto ap
    on ap.progetto = prog.id
join persona p
    on p.id = ap.id
where p.posizione = 'Professore Ordinato'
group by p.id, p.nome, p.cognome

--corretta
select p.id, p.nome, p.congome, count(distinct ap.progetto)
from persona p
    join AttivitàProgetto ap
    on ap.persona = p.id
where p.posizione = 'Professore Ordinato'

-- 6. Qual è il numero di assenze per malattia di ogni
-- professore associato. Per ogni professore associato,
-- restituire nume, cognome e numero di assenze per
-- malattia [3 punti]

select p.id, p.nome, p.cognome, count(distinct a.id)
from assenza a
join persona p
    on p.id = a.persona
where p.posizione = 'Professore Associato'
    and a.tipo = 'Malattia'
group by p.id, p.nome, p.cognome

-- 7. Qual è il numero totale di ore, per ogni persona, dedicate
-- al progetto con id ‘5’. Per ogni persona che lavora al
-- progetto, restituire nome, cognome e numero di ore totali
-- dedicate ad attività progettuali relative al progetto 
-- [4 punti]

select sum(ap.oreDurata), p.id, p.nome, p.cognome
from persona p
join AttivitàProgetto ap
    on p.id = ap.persona
join progetto prog
    on prog.id = ap.progetto
where prog.id = 5
group by p.id, p.nome, p.cognome

--corretta
select p.nome, p.cognome, sum(ap.oreDurata)
from persona p
    join AttivitàProgetto ap
    on ap.persona = p.id
where ap.progetto = 5
group by p.id

-- 8. Qual è il numero medio di ore delle attività progettuali
-- svolte da ogni persona. Per ogni persona, restituire nome,
-- cognome e numero medio di ore delle sue attività
-- progettuali (in qualsivoglia progetto) [3 punti]

select avg(ap.oreDurata), p.id, p.nome, p.cognome
from AttivitàProgetto ap
join persona p
    on p.id = ap.persona
group by p.id, p.nome, p.cognome

--corretta
select p.nome, p.cognome, sum(ap.oreDurata)
from persona p
    join AttivitàProgetto ap
    on ap.persona = p.id
where ap.progetto = 5
group by p.id

--verifica


-- 9. Qual è il numero totale di ore, per ogni persona, dedicate
-- alla didattica. Per ogni persona che ha svolto attività
-- didattica, restituire nome, cognome e numero di ore totali
-- dedicate alla didattica [4 punti]

select sum(distinct ap.oreDurata), p.id, p.nome, p.cognome
from persona p
join AttivitàNonProgettuale anp
    on anp.persona = p.id
where anp.tipo = 'Didattica'
group by p.id, p.nome, p.cognome
having sum(distinct ap.oreDurata) > 0
-- where anp.id is not null

-- 10. Quali sono le persone che hanno svolto attività nel WP
-- di id ‘5’ del progetto con id ‘3’. Per ogni persona, restituire
-- il numero totale di ore svolte in attività progettuali per il
-- WP in questione [4 punti]

select p.id, p.nome, p.cognome, sum(ap.oreDurata)
from persona p
join AttivitàProgetto ap
    on ap.persona = p.id
join wp 
    on wp.progetto = ap.progetto
where wp.progetto = 3
    and wp.id = 5
group by p.id, p.nome, p.cognome

--corretta
select p.id, p.nome, p.cognome, sum(ap.oreDurata)


-- non testate
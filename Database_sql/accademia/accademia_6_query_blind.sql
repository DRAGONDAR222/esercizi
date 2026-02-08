
-- 1

select count(p.id), p.posizione
from persona p 
group by p.posizione

-- 2

select count(p.id), p.posizione
from persona p 
where p.stipendio >= 40000
group by p.posizione


-- 3

select count(prog.id)
from progetto prog
where prog.fine < current_date
    and prog.budget > 50000

-- 4

select min(ap.oreDurata), max(ap.oreDurata), avg(ap.oreDurata)
from AttivitàProgetto ap join progetto prog
    on ap.progetto = prog.id
where prog.nome = 'Pegasus'

-- 5 

select p.id, p.nome, p.cognome,
       min(ap.oreDurata) as ore_min,
       max(ap.oreDurata) as ore_max,
       avg(ap.oreDurata) as ore_media
from AttivitàProgetto ap
join progetto prog
  on ap.progetto = prog.id
join persona p
  on ap.persona = p.id
where prog.nome = 'Pegasus'
  and (p.posizione = 'Professore Ordinario'
  or p.posizione =  'Professore Associato')
group by p.id;


-- 6 

select sum(ap.oreDurata), p.id,p.nome,p.cognome
from AttivitàProgetto ap join persona p
    on p.id = ap.persona
where ap.tipo = 'Didattica'
    and (p.posizione = 'Professore Ordinario'
    or p.posizione =  'Professore Associato')
group by p.id


-- 7

select avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from persona p
where p.posizione = 'Ricercatore'

-- 8 

select avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from persona p
group by p.posizione

-- 9

select sum(ap.oreDurata), ap.progetto
from AttivitàProgetto ap join persona p
    on p.id = ap.persona
where p.nome = 'Ginevra'
    and p.cognome = "Riva"
group by ap.progetto


-- 10 

select prog.nome
from AttivitàProgetto ap join persona p 
    on p.id = ap.persona
join Progetto prog 
    on ap.progetto = prog.id
group by prog.id, prog.nome
having count(distinct p.id) > 2;


-- 11

select p.id, p.nome, p.cognome
from persona p
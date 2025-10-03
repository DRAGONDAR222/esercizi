-- 1. Quanti sono gli strutturati di ogni fascia

select p.posizione, count(*)
from Persona p
group by posizione;

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count(*)
from Persona p
where p.stipendio >= 40000


-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(prog.nome)
from Progetto prog
where prog.fine < current_date
and prog.budget > 50000;


-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
-- ‘Pegasus’ ?

select avg(atp.oreDurata), max(atp.oreDurata), min(atp.oreDurata)
from Progetto prog, Attivitàprogetto atp
where atp.progetto = prog.id
and prog.nome = 'Pegasus'


-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?

select p.id, p.nome, p.cognome, avg(atp.oreDurata), max(atp.oreDurata), min(atp.oreDurata)
from Progetto prog, Attivitàprogetto atp, Persona p
where atp.progetto = prog.id
and prog.nome = 'Pegasus'
and p.id = atp.persona
group by(p.id)


-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select p.id, p.nome, p.cognome, sum(atnp.oreDurata)
from Persona p, AttivitàNonProgettuale atnp
where atnp.tipo = 'Didattica'
and atnp.persona = p.id
group by(p.id)


-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from Persona p
where p.posizione = 'Ricercatore'


-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
-- associati e dei professori ordinari?

select p.posizione, avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from Persona p
group by (p.posizione)


-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select prog.nome, SUM(atp.oredurata)
from attivitàprogetto atp, progetto prog, persona p
where atp.progetto = prog.id
and atp.persona = p.id
and p.nome = 'Ginevra Riva'
group by prog.nome


-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select prog.id, prog.nome
from attivitàprogetto atp, progetto prog, persona p
where atp.progetto = prog.id
and atp.persona = p.id
group by prog.id, prog.nome
having count(distinct p.id) > 2


-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?

select p.id, p.nome, p.cognome
from persona p, attivitàprogetto atp
where p.id = atp.persona
and p.posizione = 'Professore Associato'
group by p.id, p.nome, p.cognome
having count(distinct atp.progetto) > 1;


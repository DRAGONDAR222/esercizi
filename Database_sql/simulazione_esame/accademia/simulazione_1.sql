-- 1. Elencare tutti i progetti la cui fine è successiva al
-- 2023-12-31. [2 punti]

select *
from progetto p
where p.fine > 2023-12-31

-- 2. Contare il numero totale di persone per ciascuna posizione
-- (Ricercatore, Professore Associato, Professore Ordinario).
-- [3 punti]

select p.posizione,count(distinct p.id)
from persona p
group by p.posizione

-- 3. Restituire gli id e i nomi delle persone che hanno almeno
-- un giorno di assenza per "Malattia". [2 punti]

select p.id, p.nome
from persona p 
join assenza 
    on p.id = a.persona
where a.tipo = 'Malattia'

-- 4. Per ogni tipo di assenza, restituire il numero complessivo
-- di occorrenze. [3 punti]

select a.tipo, count(distinct a.id)
from assenza a
group by a.tipo


-- 5. Calcolare lo stipendio massimo tra tutti i "Professori
-- Ordinari". [2 punti]

select max(p.stipendio)
from persona p
where p.posizione = 'Professore'


-- 6. Quali sono le attività e le ore spese dalla persona con id 1
-- nelle attività del progetto con id 4, ordinate in ordine
-- decrescente. Per ogni attività, restituire l’id, il tipo e il
-- numero di ore. [3 punti]

select ap.id, ap.tipo, ap.oreDurata
from AttivitàProgetto ap
where ap.persona = 1
  and ap.progetto = 4
order by ap.oreDurata desc;


-- 7. Quanti sono i giorni di assenza per tipo e per persona. Per
-- ogni persona e tipo di assenza, restituire nome, cognome,
-- tipo assenza e giorni totali. [4 punti]

select p.nome,p.cognome,a.tipo, count(distinct a.giorno)
from assenza a
join persona p
    on p.id = a.persona
group by p.nome,p.cognome,a.tipo


-- 8. Restituire tutti i “Professori Ordinari” che hanno lo
-- stipendio massimo. Per ognuno, restituire id, nome e
-- cognome [4 punti]

select p.stipendio, p.id, p.nome, p.cognome, 
from persona p
where p.posizione = 'Professore Ordinato'
group by p.id, p.nome, p.cognome, p.stipendio
having p.stipendio = (select max(p.stipendio)
                        from persona p
                        where p.posizione = 'Professore Ordinato')


-- 9. Restituire la somma totale delle ore relative alle attività
-- progettuali svolte dalla persona con id = 3 e con durata
-- minore o uguale a 3 ore. [3 punti]

select sum(ap.oreDurata)
from AttivitàProgetto ap
join persona p
    on p.id = anp.persona
where p.id = 3
and ap.oreDurata <= 3 * 60
group by ap.id


-- 10. Restituire gli id e i nomi delle persone che non hanno
-- mai avuto assenze di tipo "Chiusura Universitaria" [4
-- punti]

select p.id, p.nome
from persona p 
left join assenza a
    on p.id = a.persona
    and a.id is null 
where a.tipo = 'Chiusura Universitaria'

-- non testate

-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
-- aeroporti?

select a.codice, a.nome as aeroporto, count(distinct comp) as n_compagnie
from arrpart ap, aeroporto a
where (a.codice = ap.partenza or a.codice = ap.arrivo)
group by a.codice, a.nome;


-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
-- 100 minuti?

select count(*)
from volo v, arrpart ap
where v.codice = ap.codice 
	and v.comp = ap.comp -- !
	and ap.partenza = 'HTR'
	and v.durataminuti >= 100;


-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
-- nella quale opera?

select nazione, count(distinct l.aeroporto)
from arrpart ap, luogoaeroporto l
where (l.aeroporto = ap.partenza or l.aeroporto = ap.arrivo)
	and ap.comp = 'Apitalia'
group by l.nazione;


-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
-- compagnia ‘MagicFly’ ?

select round(avg(durataminuti), 2) as durata_media, 
		min(durataminuti) as durata_min, 
		max(durataminuti) as durata_max from volo
where comp = 'MagicFly';


-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
-- aeroporti?

select a.codice, a.nome, min(c.annofondaz) as anno_piu_vecchia
from arrpart ap, aeroporto a, compagnia c
where (a.codice = ap.partenza or a.codice = ap.arrivo)
	and ap.comp = c.nome
group by a.codice, a.nome;


-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione 
-- tramite uno o più voli?

select lap.nazione as nazione_partenza, count(distinct laa.nazione) as raggiungibili
from luogoaeroporto lap, arrpart ap, luogoaeroporto laa
where lap.aeroporto = ap.partenza
	and ap.arrivo = laa.aeroporto
	and lap.nazione <> laa.nazione
group by lap.nazione;


-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select a.codice, a.nome, round(avg(v.durataminuti), 2) as durata_media
from volo v, aeroporto a, arrpart ap
where v.codice = ap.codice 
	and v.comp = ap.comp 
	and a.codice = ap.partenza
group by a.codice, a.nome;


-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
-- a partire dal 1950?
select c.nome as compagnia, sum(durataminuti) as durata_totale
from volo v, compagnia c
where v.comp = c.nome
	and annofondaz >= 1950
group by c.nome;


-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select a.codice, a.nome as aeroporto
from arrpart ap, aeroporto a
where (a.codice = ap.partenza or a.codice = ap.arrivo)
group by a.codice, a.nome
having count(distinct ap.comp) = 2;


-- 10. Quali sono le città con almeno due aeroporti?

select citta
from luogoaeroporto 
group by citta
having count(*) >= 2;


-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?

select v.comp
from volo v
group by v.comp
having avg(durataminuti) > 6*60;


-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?

select v.comp
from volo v
group by v.comp
having min(durataminuti) > 100;


-- 13. Qual è il nome delle compagnie che hanno il volo più lungo?

with D as (
	select max(durataminuti) as max_durata
	from volo
)
-- D è una tabella 1x1 con una sola colonna 'max_durata'
select comp
from volo, D -- risulta in una tabella in cui ogni ennupla è una ennupla di 'volo' con
			-- anche il valore 'D.max_durata'
group by comp, D.max_durata
having max(durataminuti) > D.max_durata;


-- alternativa
with D as
(
select max(durataminuti) as max_durata
from volo)
select distinct v.comp
from volo v, D
where v.durataminuti = D.max_durata;


-- 14. qual è il nome delle compagnie che non hanno alcun volo?

-- tutte le compagnie che hanno almeno un volo
with D as (
	select distinct part.comp
	from volo v, arrpart part       
	where part.codice = v.codice
	and part.comp = v.comp
)

-- confronto con tutte le compagnie
select distinct comp.nome
from compagnia comp
where comp.nome not in (select * from D) -- per ogni compagnia in D

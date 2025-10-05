-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
-- aeroporti?

select a.codice,
    (select count(distinct ar.comp)
    from arrpart ar
    where ar.arrivo = a.codice
    or ar.partenza = a.codice)
from aeroporto a


-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
-- 100 minuti?

select count(v.codice)
from volo v, arrpart ar
where v.durataminuti > 100
and ar.codice = v.codice
and ar.comp = v.comp
and ar.partenza = 'HTR'


-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
-- nella quale opera?

select luogo.nazione, count(distinct aero.codice)
from arrpart part, aeroporto aero, luogoaeroporto luogo
where part.comp = 'Apitalia'
and (part.partenza = aero.codice or part.arrivo = aero.codice)
and aero.codice = luogo.aeroporto
group by luogo.nazione;


-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
-- compagnia ‘MagicFly’ ?

select max(v.durataminuti),min(v.durataminuti), avg(v.durataminuti)
from volo v, arrpart part
where part.codice = v.codice
and part.comp = v.comp
and part.comp = 'MagicFly'


-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
-- aeroporti?

select min(comp.annofondaz), aero.nome, aero.codice
from compagnia comp, arrpart part, aeroporto aero
where comp.nome = part.comp
group by(aero.codice)


-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
-- voli?


select count(distinct luogo1.nazione)
from luogoaeroporto luogo1, arrpart part, luogoaeroporto luogo2
where part.arrivo = luogo1.aeroporto
group by(part.codice, part.comp) 


-- da terminare 

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select distinct aero.codice,aero.nome, avg(v.durataminuti)
from aeroporto aero, arrpart part, volo v
where aero.codice = part.partenza 
and v.codice = part.codice
group by(aero.codice)


-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
-- a partire dal 1950?

select comp.nome, sum(v.durataminuti)
from volo v, arrpart part, compagnia comp
where comp.annofondaz >= 1950
and part.comp = comp.nome
and v.codice = part.codice
and v.comp = part.comp
group by(comp.nome)


-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select distinct aero.nome, aero.codice
from aeroporto aero, arrpart part, compagnia comp
where (aero.codice = part.partenza or aero.codice = part.arrivo)
and comp.nome = part.comp
group by(aero.nome, aero.codice)
having count(distinct comp.nome) = 2


-- 10. Quali sono le città con almeno due aeroporti?

select luogo.citta
from luogoaeroporto luogo, aeroporto aero
where aero.codice = luogo.aeroporto
group by(luogo.citta)
having count(distinct aero.codice) >= 2


-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
-- ore?

select comp.nome
from compagnia comp, arrpart part, volo v
where part.comp = comp.nome 
and v.codice = part.codice
and v.comp = part.comp
group by(comp.nome)
having avg(v.durataminuti) > 6 * 60


-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
-- minuti?

select comp.nome
from compagnia comp, arrpart part, volo v
where part.comp = comp.nome 
and v.codice = part.codice
and v.comp = part.comp
group by(comp.nome)
having min(v.durataminuti) > 100

-- 1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore

select v.codice, c.nome
from compagnia c,volo v
where v.durataMinuti > 180
and c.nome = v.comp

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?

select distinct c.nome
from compagnia c,volo v
where v.durataMinuti > 180
and c.nome = v.comp

-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
-- codice ‘CIA’ ?

select distinct v.codice, part.comp
from volo v, arrpart part, aeroporto aero
where v.codice = part.codice and v.comp = part.comp
and part.partenza = aero.codice
and aero.codice = 'CIA'


-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
-- ‘FCO’ ?

select distinct v.codice, part.comp
from volo v, arrpart part, aeroporto aero
where v.codice = part.codice and v.comp = part.comp
and part.arrivo = aero.codice
and aero.codice = 'FCO'

-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
-- e arrivano all’aeroporto ‘JFK’ ?


select distinct v.codice, part.comp
from volo v, arrpart part, aeroporto aero1, aeroporto aero2
where v.codice = part.codice and v.comp = part.comp
and part.partenza = aero1.codice
and part.arrivo = aero2.codice
and aero1.codice = 'FCO'
and aero2.codice = 'JFK'

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atter-
-- rano all’aeroporto ‘JFK’ ?

select distinct part.comp
from volo v, arrpart part, aeroporto aero1, aeroporto aero2
where v.codice = part.codice and v.comp = part.comp
and part.partenza = aero1.codice
and part.arrivo = aero2.codice
and aero1.codice = 'FCO'
and aero2.codice = 'JFK'

-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
-- città di ‘New York’ ?

select distinct part.comp
from volo v, arrpart part, luogoaeroporto l1, luogoaeroporto l2
where v.codice = part.codice and v.comp = part.comp
and part.partenza = l1.aeroporto
and part.arrivo = l2.aeroporto
and l1.citta = 'Roma'
and l2.citta = 'New York'

-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
-- della compagnia di nome ‘MagicFly’ ?

select distinct aero.codice, aero.nome, l.citta 
from aeroporto aero, luogoaeroporto l, arrpart ap
where ap.comp = 'MagicFly'
and aero.codice = l.aeroporto
and ap.partenza = aero.codice

-- 9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
-- atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
-- del volo, nome della compagnia, e aeroporti di partenza e arrivo.

select distinct part.comp, part.codice, part.partenza, part.arrivo
from volo v, arrpart part, luogoaeroporto l1, luogoaeroporto l2
where v.codice = part.codice and v.comp = part.comp
and part.partenza = l1.aeroporto
and part.arrivo = l2.aeroporto
and l1.citta = 'Roma'
and l2.citta = 'New York'

-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
-- voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
-- qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
-- codici dei voli, e aeroporti di partenza, scalo e arrivo.

select distinct *
from arrpart ar1, arrpart ar2, luogoaeroporto l1, luogoaeroporto l2
where ar1.comp = ar2.comp
and ar1.partenza = l1.aeroporto
and ar2.arrivo = l2.aeroporto
and ar1.arrivo = ar2.partenza
and l1.citta = 'Roma'
and l2.citta = 'New York'

-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
-- rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

select distinct comp.nome
from arrpart ar, compagnia comp
where comp.annoFondaz is not null
and ar.partenza = 'FCO'
and ar.arrivo = 'JFK'
and ar.comp = comp.nome
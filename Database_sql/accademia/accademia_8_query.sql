-- 1. Quali sono le persone (id, nome e cognome) che hanno avuto assenze solo nei
-- giorni in cui non avevano alcuna attivitÃ (progettuali o non progettuali)?

SELECT DISTINCT p.id, p.nome, p.cognome
FROM persona p
LEFT JOIN assenza a
    ON a.persona = p.id
LEFT JOIN attivitàprogetto ap
    ON ap.persona = a.persona
   AND ap.giorno = a.giorno
LEFT JOIN attivitànonprogettuale anp
    ON anp.persona = a.persona
   AND anp.giorno = a.giorno
GROUP BY p.id, p.nome, p.cognome
HAVING COUNT(ap.id) + COUNT(anp.id) = 0
ORDER BY p.id;


-- 2. Quali sono le persone (id, nome e cognome) che non hanno mai partecipato ad
-- alcun progetto durante la durata del progetto “Pegasus”?



-- 3. Quali sono id, nome, cognome e stipendio dei ricercatori con stipendio maggiore
-- di tutti i professori (associati e ordinari)?



-- 4. Quali sono le persone che hanno lavorato su progetti con un budget superiore alla
-- media dei budget di tutti i progetti?



-- 5. Quali sono i progetti con un budget inferiore allala media, ma con un numero
-- complessivo di ore dedicate alle attività di ricerca sopra la media?
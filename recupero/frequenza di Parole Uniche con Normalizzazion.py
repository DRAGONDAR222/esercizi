'''Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.
Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}'''


def normalizza(testo:str) -> dict:

    my_dict:dict = {}
    testo = testo.strip(",!?.").lower()
    testo_diviso:list[str] = testo.split()

    for elemento in testo_diviso:
        elemento.strip(",!?.")
        if elemento not in my_dict:
            my_dict[elemento] = 1
        else:
            my_dict[elemento] += 1

    return my_dict


print(normalizza("Hello, world! Hello... PYTHON? world."))



    
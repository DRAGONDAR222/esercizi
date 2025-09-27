'''Scrivi una funzione pulisci_testo(testo: str) -> dict[str, int] che:

    Pulisce il testo da punteggiatura e simboli speciali

    Rende tutte le lettere minuscole

    Conta la frequenza di ogni parola presente nel testo

    Restituisce un dizionario con le parole come chiavi e il numero di occorrenze come valore'''

def pulisci_testo(testo: str) -> dict[str, int]:
    testo_pulito: str = ''

    for i in range(len(testo)):
        if testo[i].isalpha() or testo[i].isnumeric() or testo[i] == ' ':
            testo_pulito += testo[i].lower()

    parole = testo_pulito.split()
    
    conteggio: dict[str, int] = {}

    for parola in parole:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

    return conteggio

    
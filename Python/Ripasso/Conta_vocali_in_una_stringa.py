'''Scrivi una funzione ricorsiva conta_vocali(s: str) -> int che:

    prende una stringa s,

    conta e restituisce il numero totale di vocali (a, e, i, o, u, maiuscole o minuscole) presenti nella stringa,

    senza usare cicli (for/while), solo ricorsione.'''



def conta_vocali(s: str) -> int:
    vocali = 'aeiou'

    if len(s) == 0:
        return 0

    primo = 1 if s[0].lower() in vocali else 0
    return primo + conta_vocali(s[1:])

    
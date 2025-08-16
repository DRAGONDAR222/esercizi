'''Scrivi una funzione:

def analizza_vocali(testo: str) -> dict[str, int]:

Che:

    Riceve una stringa testo (può contenere lettere, spazi, numeri, simboli).

    Conta quante volte compaiono le vocali (a, e, i, o, u) ignorando maiuscole/minuscole.

    Restituisce un dizionario con la frequenza di ogni vocale presente almeno una volta.'''


import re

def analizza_vocali(testo: str) -> dict[str, int]:
    my_dict:dict[str,int] = {'a':0,'e':0,'i':0,'o':0,'u':0}

    for i in testo:
        if re.search(r'A',i.upper()):
            my_dict['a'] += 1
        if re.search(r'E',i.upper()):
            my_dict['e'] += 1
        if re.search(r'I',i.upper()):
            my_dict['i'] += 1
        if re.search(r'O',i.upper()):
            my_dict['o'] += 1
        if re.search(r'U',i.upper()):
            my_dict['u'] += 1

    return my_dict
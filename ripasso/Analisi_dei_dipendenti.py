'''Hai una lista di dizionari che rappresentano dei dipendenti di un'azienda:

dipendenti = [
    {"nome": "Luca", "cognome": "Rossi", "età": 34, "stipendio": 2700.50},
    {"nome": "Anna", "cognome": "Verdi", "età": 29, "stipendio": 3100.00},
    {"nome": "Marco", "cognome": "Bianchi", "età": 45, "stipendio": 2500.75},
    {"nome": "Sara", "cognome": "Gialli", "età": 52, "stipendio": 4000.00},
    {"nome": "Elena", "cognome": "Neri", "età": 41, "stipendio": 2900.20},
]

Obiettivo:

Scrivi una funzione analizza_dipendenti(dipendenti: list[dict]) -> dict che restituisce un dizionario con:

    "media_stipendio": media arrotondata degli stipendi

    "più_anziano": stringa "Nome Cognome (età)" del dipendente più anziano

    "sopra_media": lista ordinata per stipendio decrescente con i soli dipendenti che guadagnano più della media

    "iniziano_con_vocale": numero di dipendenti il cui nome inizia con una vocale'''


dipendenti = [
    {"nome": "Luca", "cognome": "Rossi", "età": 34, "stipendio": 2700.50},
    {"nome": "Anna", "cognome": "Verdi", "età": 29, "stipendio": 3100.00},
    {"nome": "Marco", "cognome": "Bianchi", "età": 45, "stipendio": 2500.75},
    {"nome": "Sara", "cognome": "Gialli", "età": 52, "stipendio": 4000.00},
    {"nome": "Elena", "cognome": "Neri", "età": 41, "stipendio": 2900.20},
]


def analizza_dipendenti(dipendenti: list[dict]) -> dict:
    my_dict:dict = {'media_stipendio':0.00,'più_anziano':'','sopra_media':[],'iniziano_con_vocale':0}

    for i in dipendenti:
        my_dict['media_stipendio'] += i['stipendio']

    my_dict['media_stipendio'] = round(my_dict['media_stipendio'] / len(dipendenti),2)


    piu_anziano = max(dipendenti, key=lambda x: x['età'])
    my_dict['più_anziano'] = f"{piu_anziano['nome']} {piu_anziano['cognome']} ({piu_anziano['età']})"

    sopra_media = list(filter(lambda x: x['stipendio'] > my_dict['media_stipendio'], dipendenti))
    ordinati = sorted(sopra_media, key=lambda x: x['stipendio'], reverse=True)

    my_dict['sopra_media'] = [f"{x['nome']} {x['cognome']}" for x in ordinati]

    vocali:str = 'AEIOU'
    my_dict['iniziano_con_vocale'] = sum(1 for x in dipendenti if x['nome'][0].upper() in vocali)

    return my_dict

'''Scrivi una funzione analizza_parole(lista_parole: list[str]) -> dict[str, list[str]] che:

    Prende una lista di parole (stringhe).

    Seleziona le parole "valide", che:

        Hanno almeno 5 lettere,

        Contengono solo lettere alfabetiche (niente numeri o simboli),

        Non contengono lettere ripetute (es. "piano" va bene, "cassa" no).

    Ritorna un dizionario con:

        Chiave "valide" → lista delle parole valide

        Chiave "scartate" → lista delle parole scartate'''

def analizza_parole(lista_parole: list[str]) -> dict[str, list[str]]:
    my_dict: dict[str, list[str]] = {"valide": [], "scartate": []}

    for parola in lista_parole:
        if len(parola) >= 5 and parola.isalpha() and len(set(parola)) == len(parola):
            my_dict["valide"].append(parola)
        else:
            my_dict["scartate"].append(parola)

    return my_dict

                 
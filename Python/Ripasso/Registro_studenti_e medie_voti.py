'''Scrivi una funzione:

def analizza_studenti(registro: dict[str, list[int]]) -> dict[str, float]:

Che:

    Riceve un dizionario dove:

        Le chiavi sono i nomi degli studenti,

        I valori sono liste di voti (interi tra 0 e 10).

    Restituisce un nuovo dizionario dove:

        Ogni studente ha come valore la media dei suoi voti, arrotondata a 2 cifre decimali.

    Scarta eventuali studenti che:

        Hanno una lista vuota,

        Oppure hanno più di un voto fuori dal range 0–10.'''

def analizza_studenti(registro: dict[str, list[int]]) -> dict[str, float]:

    my_dict: dict[str, float] = {}

    for i in registro:
        if not registro[i]:
            continue
        else:
            count: int = 0
            voti_validi: list[int] = []

            for j in registro[i]:
                if j not in range(0, 11):
                    count += 1
                else:
                    voti_validi.append(j)

            if count < 2 and voti_validi:
                my_dict[i] = round(sum(voti_validi) / len(voti_validi), 2)

    return my_dict

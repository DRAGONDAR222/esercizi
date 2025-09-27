'''Scrivi una funzione raggruppa_giudizi(voti: list[int]) -> dict[str, list[int]] che prende in input una lista di voti (da 0 a 10) e restituisce un dizionario in cui i voti sono suddivisi per giudizio secondo questi criteri:
Giudizio	Voto
"insufficiente"	0–5
"sufficiente"	6
"buono"	7–8
"ottimo"	9–10'''

def raggruppa_giudizi(voti: list[int]) -> dict[str, list[int]]:

    giudizi:dict[str, list[int]] = {'insufficiente':[],'sufficiente':[],'buono':[],'ottimo':[]}

    for i in voti:
        if i in range(0,6):
            giudizi['insufficiente'].append(i)
        if i == 6:
            giudizi['sufficiente'].append(i)
        if i in range(7,9):
            giudizi['buono'].append(i)
        if i in range(9,11):
            giudizi['ottimo'].append(i)
    return giudizi  
        
        
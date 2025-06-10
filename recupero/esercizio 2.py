'''2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.'''

def classifica(list:list[int | float])-> dict[list]:

    dizionario_1:dict = {'positivi': [],'negativi': []}
    for elemento in list:
        if elemento >= 0:
            dizionario_1['positivi'].append(elemento)
        else:
            dizionario_1['negativi'].append(elemento)
    return dizionario_1


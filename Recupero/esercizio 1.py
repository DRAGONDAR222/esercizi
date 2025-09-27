'''1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.'''



def converti(list:list[tuple]) -> dict:
    my_dict:dict = {}
    for tupla in list:
        if tupla[0] not in my_dict:
            my_dict[tupla[0]] = tupla[1]
        else:
            my_dict[tupla[0]] += tupla[1]
    return my_dict
    

print(converti([("0",1),("1",1),("1",1)]))
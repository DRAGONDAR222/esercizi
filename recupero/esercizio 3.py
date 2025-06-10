'''3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''


def prodotti(dict1:dict)->dict:

    new_dict:dict = {}
    for prodotto in dict1:
        if dict1[prodotto] < 50:
            a:float = dict1[prodotto]
            a += (a * 10)/100
            a = round(a,2)
            new_dict[prodotto] = a
    return new_dict 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
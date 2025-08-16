'''Esercizio 2.

Si vuole calcolare la somma di tutti i prodotti x * y per tutti i valori interi di x (i cui valori variano tra 0 e 100) e tutti i valori interi di y 
(i cui valori sono dati dalla sequenza 2, 4, 6, 8, 10, 12, ..., 88), ovvero i prodotti
1 * 2,
1 * 4,
...
1 * 88,
2 * 2,
2 * 4,
...
2 * 88,
...
100 * 2,
100 * 4,
...
100 * 88

Scrivere una funzione Python proDict() che senza ricevere alcun argomento in input, che restituisce un dizionario che abbia come chiavi la tupla (x,y)
 e come valore x*y , in cui memorizzare tutti i prodotti x * y per tutti i valori interi di x e tutti i valori interi di y.

Nel main, scrivere un codice Python che inizializzi un dizionario d ricorrendo alla funzione prodDict e stampare
 in output i valori del dizionario d, per i seguenti valori di x e y:

    x = 13, y = 88

    x = 83, y = 56

    x = 71, y = 44

'''

def proDict() -> dict[tuple[int, int], int]:
    my_dict: dict[tuple[int, int], int] = {}
    
    for x in range(0, 100+1):
        for y in range(2, 88+1, 2):
            my_dict[(x, y)] = x * y
            
    return my_dict


if __name__ == "__main__":

    d = proDict()

    print("x = 13, y = 88 ->", d[(13, 88)])
    print("x = 83, y = 56 ->", d[(83, 56)])
    print("x = 71, y = 44 ->", d[(71, 44)])





    


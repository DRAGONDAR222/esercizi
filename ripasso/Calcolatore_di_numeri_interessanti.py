'''Scrivi una funzione numeri_interessanti(start, end) che:

    Riceve due numeri interi start e end.

    Crea una lista di tutti i numeri tra start ed end inclusi.

    Considera "interessanti" i numeri che:

        Sono pari,

        Divisibili per 3 o 5,

        E non contengono la cifra 4.

    Restituisce una lista di questi numeri "interessanti".

    numeri_interessanti(10, 30)
    [12, 15, 18, 20, 24, 30]

    
    Scrivi anche una versione con list comprehension.

    Aggiungi un contatore che stampa quanti numeri sono stati scartati perché contenevano un 4.
    '''


def numeri_interessanti(start:int,end:int) -> tuple[list[int], list[int]]:
    n_interessanti:list[int] = []
    n_scartati:list[int] = []

    for i in range(start,end+1):
        if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0) and "4" not in str(i):
            n_interessanti.append(i)
        if "4" in str(i):
            n_scartati.append(i)


    return n_interessanti,n_scartati


        
print(numeri_interessanti(10, 30))





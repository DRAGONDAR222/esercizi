'''Scrivi una funzione ricorsiva inverti_lista(lista: list[int]) -> list[int] che:

    prende una lista di interi,

    restituisce una nuova lista con gli elementi in ordine inverso,

    senza usare cicli (for/while) e senza usare metodi built-in come .reverse() o slicing con step negativo,

    solo ricorsione.'''

def inverti_lista(lista: list[int]) -> list[int]:
    if len(lista) <= 1:
        return lista  
    else:
        return [lista[-1]] + inverti_lista(lista[:-1])
    
    

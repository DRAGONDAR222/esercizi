'''Scrivi una funzione ricorsiva conta_elemento(lista: list, elemento) -> int che:

    prende una lista che può contenere elementi singoli o altre liste annidate a qualsiasi profondità,

    conta quante volte elemento appare in tutta la struttura (compresi gli elementi dentro le sottoliste),

    usa la ricorsione per scorrere anche dentro le liste annidate,

    senza usare cicli (for/while), solo ricorsione.'''


def conta_elemento(lista: list, elemento) -> int:
    if not lista:
        return 0

    if isinstance(lista[0], list):
        
        return conta_elemento(lista[0], elemento) + conta_elemento(lista[1:], elemento)
    else:

        return (1 if lista[0] == elemento else 0) + conta_elemento(lista[1:], elemento)



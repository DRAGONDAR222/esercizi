'''Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.'''


def ricerca(num:int,my_list:list[int])-> bool:
    while my_list:

        a:int = len(my_list)//2

        if num == my_list[a]:
            return True

        elif num < my_list[a]:
            my_list = my_list[:a]      

        elif num > my_list[a]:
            my_list = my_list[a + 1:]

    return False
        

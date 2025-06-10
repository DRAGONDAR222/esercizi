'''1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.'''



def verifica(X,Y,Z)->str:
    if X == True and Y or Z == True:
        return "Azione permessa"
    return "Azione negata"

'''2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.'''

def moltiplica(my_list:list[int | float],threshold:int)->list[int | float]:
    for i in range(len(my_list)):
        if my_list[i] < threshold and isinstance(my_list[i], int):
            a:int = my_list[i] * threshold
            my_list[i] = a
    return my_list
             
'''3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45'''

for i in range(2, 15, 2):
    print(i)

for i in range(1, 14, 3):
    print(i)

for i in range(30, -1, -5):
    print(i)

for i in range(5, 50, 10):
    print(i)


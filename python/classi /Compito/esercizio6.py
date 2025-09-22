'''Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2,
e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

risultato:int = 0

print("scrivi 2 numeri")
a = int(input())
b = int(input())
n1 = min(a , b)    # così facendo mi assicuro che "a" sia SEMPRE il più piccolo tra i numeri
n2 = max(a , b)

risultato:int = n1    # partiamo dall' n1 iniziale per far si che la prima moltiplicazione non risulti 0

while True:
    if n1 != n2:        # aumento finchè non raggiungo il "valore numerico" di b (includendolo di conseguenza)
        n1 += 1
        risultato *= n1    # moltiplico il risultato precedente ad ogni ciclo
        print(risultato)
    else:
        print("il precedente è il risultato finale")
        break

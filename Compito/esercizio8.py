'''Esercizio 8
Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30)
 e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******'''


my_list = []

while len(my_list) < 5:
    print("aggiungi un elemento compreso tra 1 e 30 alla lista")
    a = int(input())            # RICORDA di scrivere le () dopo l' "input"
    if 1 <= a <= 30:           
        my_list.append(a)

print(str(my_list))             # così facendo prima scrivo la lista nel terminale (poichè viene scritta appena usciti dal ciclo "while")
 
for x in range(len(my_list)):   # imposto un ciclo "for" adoperando la variabile "x"  la funzione "range(len(my_list))" crea una sequenza di numeri che inizia dalla posizione 0 della lista e termina alla posizione len(my_list) - 1 (l'ultima)
    print('*' * my_list[x])




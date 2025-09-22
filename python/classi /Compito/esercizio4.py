'''Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali).
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''

my_list =  []                
my_list_interi = []
sum = 0
media = 0 


print("inserisci un numero, se sarà negativo il programma terminerà") 
while True:               # si attiva sempre
    a = float(input())    # obbligo l'input dell'utente ad essere un float
    if a < 0:             # siccome solo un "numero" può essere paragonato a 0 "a" deve essere un "float"
        break
    else:                   # se non una allora l'altra
        my_list.append(a)      
        if a.is_integer() == True:    # un float può essere un "integer" nel momento in cui dopo la , vi siano solo 0
            my_list_interi.append(a)
            sum += a
            print("questa è la somma degli interi " + str(sum))           # "str" scritto prima permette di tradurre a stringa il (contenuto delle parentesi)
            media = sum/len(my_list_interi)                               # "len" indica il numero di elementi presenti all'interno della lista
            print("questa è la media degli interi " + str(media))         
        print("questo è il massimo complessivo " + str(max(my_list)))     # "max" indica il massimo contenuto nella lista
        print("questo è il minimo complessivo " + str(min(my_list)))      # "min" indica il minimo contenuto nella lista

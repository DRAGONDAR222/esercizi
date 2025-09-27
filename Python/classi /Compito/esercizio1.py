'''Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''



my_list = []                                                                                            # imposto una lista vuota
print(" inserisci un termine a tua scelta, se questo sarà 'fine' il programma terminerà")
while 1:                                                                                                # creo un ciclo while infinito
    x:str = input()                                                                                     # imposto una variabile che ad ogni ripetizione del cilco cambierà
    if x != "fine":                                                                                     # se l'input sarà diverso da "fine" questo verà salvato nella lista vuota che andrà ad ampiarsi ad ogni ripetizione del ciclo
        my_list.append(x)
        print(my_list)                                                                                  # anche se non richiesto dall'ex mi assicuro che la lista venga aggiornata ad ogni ciclo
        if x[0] == x[-1]:                                                                               # con questo comando confronto il primo e l'ultimo carattere della mia "stringa di input"
            print("la parola inizia e finisce con lo stesso carattere")                                 
        elif x[0] != x[-1]:
            print("la parola non inizia e finisce con lo stesso carattere")

    elif x == "fine":
        break  

    
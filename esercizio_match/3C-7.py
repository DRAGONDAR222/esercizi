'''
Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%
'''

my_list:list[str] = []
testa:int = 0
croce:int = 0

print("digita t se è testa o c se è croce")

while len(my_list) < 8:
    lancio:str = input(str())
    if lancio == "t" or lancio == "c":
        my_list.append(lancio) 
        print("lancio " + str(len(my_list)) + ":" + lancio)
        match lancio:
            case "t":
                testa +=1
            case "c":
                croce +=1
           
                
print(str(testa))
print(str(croce))

risultato_testa:float = (int(testa)/ 8) * 100    # questo è il calcolo della percentuale
print(str(risultato_testa) + "%")
risultato_croce:float = (int(croce)/ 8) * 100
print(str(risultato_croce) + "%")

# devi implementare il :.2f per ottenere in output 2 numeri dopo la ,
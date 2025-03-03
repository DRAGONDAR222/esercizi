'''
Esercizio 3C-8. Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

Expected Output:

frase: di essere bellissimo
Output: Tu dici "di essere bellissimo"

- - - - - - - - - - - - - - - - - - - - - -

frase: ho vinto!
Output: Wow!
'''


frase:str = str(input(" digita una frase: "))

match frase[-1]:                              # uso la funzione match sull'ultimo "carattere" di "frase"
    case '?' if len(frase)%2==0:              # così facendo non ho bisogno di usare "and" per verificare 2 "condizioni"
        print("si!")                          
    case '?' if len(frase)%2!=0:              # controlla perchè il singolo ' funziona (solitamente uso i 2 "")
        print("no!")
    case '!':
        print("WOW!")
    case _:
        print("tu dici: " + frase)



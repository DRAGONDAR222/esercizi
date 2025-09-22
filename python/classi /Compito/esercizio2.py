'''Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa.
Il risultato deve essere visualizzato in output.'''

spazi = 0

print("scrivi una stringa")
a = str(input())
for carattere in a:        # imposto un ciclo "for" specificando di dover visualizzare i "caratteri" contenuti nella variabile "a"
    if carattere == " ":   # lo spazio tra " " permette di far identificare al programma lo spazio stesso
     spazi += 1
print(str(spazi))


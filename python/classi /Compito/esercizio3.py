'''Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale.
Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

risultato:str = ""

print("digita un termine da invertire")
termine:str = input()

while 1:
    termine[-1] = risultato[0]
    termine = termine[1:]
    print(termine)
    print(risultato)
    if termine == " ":
        break


    #non funge
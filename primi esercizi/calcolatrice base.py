"""fai una calcolatrice con sottrazione, somma, moltiplicazione e divisione"""


while 1:                                                # l'1 dopo il while permette di entrare sempre nel ciclo senza costrizioni
    print("digita 1 se vuoi una addizione, digita 2 se vuoi una sottrazione, digita 3 se vuoi una moltiplicazione, digita 4 se vuoi una divisione oppure digita 5 se vuoi uscire dal programma")
    operatore = int(input())
    risultato = 0
    if operatore == 1:
        print("selezione i tuoi 2 numeri")
        a = int(input())
        b = int(input())
        risultato = a + b
        print(risultato)
    elif operatore == 2:
        print("selezione i tuoi 2 numeri")
        a = int(input())
        b = int(input())
        risultato = a - b
        print(risultato)
    elif operatore == 3:
        print("selezione i tuoi 2 numeri")
        a = int(input())
        b = int(input())
        risultato = a * b 
        print(risultato)
    elif operatore == 4:
        print("selezione i tuoi 2 numeri")
        a = int(input())
        b = int(input())
        risultato = a / b
        print(risultato)
    elif operatore == 5:
       break                                          # ricorda che quando scrivi un ciclo while devi sempre inserire il "break" alla fine delle condizioni 

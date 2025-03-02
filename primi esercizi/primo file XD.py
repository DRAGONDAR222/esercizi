#int = interto float = decimali boolean = t/f string = stringa (parola) 

while 1:                                           # imposto un ciclo while RICORDA di mantenere gli spazi per attribuire i comandi al while
    print ("digita un numero")                     # dopo il print ricorda le parentesi e il doppio apice
    a = int(input())                               # imposto una variabile specificando la categoria (int) e scrivo le parentesi per impostare la variabile 
    print ("digita un numero")                     # scrivo prima il print per estetica afficnè l'utente digiti il comando sotto il testo 
    b = int(input())                               # quando si vuole leggere l'input dell'utente RICORDA di mettere le parentesi dopo l'input
    sum = a + b 
    print (sum)
    print ("se vuoi uscire digita finito")
    end = str(input())                             # end è una variabile stringa
    if end == 'finito':                            # if è una condizione / == significa:  se ... corrisponde a ...
        break                                      # break sarebbe l'uscita dal ciclo/ false della condizione
'''1-1. Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare 1.0/x memorizzare il risultato nella variabile y.
    Visualizzare il valore di x, y e il prodotto tra x e y.
    Sottrarre x dal prodotto tra x e y e mostrarne il risultato.'''


x = float(2.2)
y = 1.0/x
print(x)
print(y)
prodotto = float(x*y)
print(prodotto)
risultato = float(prodotto - x)
print(risultato)
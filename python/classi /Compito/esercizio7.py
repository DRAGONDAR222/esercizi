'''Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n,
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c'''


a = []
b = []
c = []

print("scirvi il quantitavio di elementi che le liste a,b dovranno contenere corrispettivamente")
lunghezza_lista = int(input()) 

while len(a) < lunghezza_lista:                  # sia in a che in b il ciclo si ripete tante volte quante indicate nel "contatore"
    print("inserisci un valore in a")
    a.append(int(input()))
    print(str(a))

while len(b) < lunghezza_lista:
    print("inserisci un valore in b")
    b.append(int(input()))
    print(str(b))      

for x in range(0, len(a)):                       # adopero un ciclo "for" con "x" (neccessaria nel caso degli interi) range è una funzione che attraverso i valori digitati nella parentesi itererà il ciclo partendo dalla posizione 0 fino a raggiungere l'ultimo elemento in "a" (len(a))
    somma = a[x] + b[lunghezza_lista-1-x]        # aggiorno la "somma" ad ogni ciclo partendo dal primo elemento in "a" a[x] (andando avanti) e partendo dall' ultimo elemento in "b" b[lunghezza_lista-1-x] andando indietro 
    c.append(somma)

print("questa è c")
print(str(c))

print(str(lunghezza_lista))
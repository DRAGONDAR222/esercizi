'''
Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e,
utilizzando un match statement, identifichi a quale categoria esso appartiene. 
L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,
mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.

Expected Output:

Digita il nome di un animale: cane
Output: cane appartiene alla categoria dei Mammiferi!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: coccodrillo
Output: coccodrillo appartiene alla categoria dei Rettili!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: pappagallo
Output: pappagallo appartiene alla categoria degli Uccelli!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: squalo
Output: squalo appartiene alla categoria dei Pesci!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: giraffa
Output: Non so dire in quale categoria classificare l'animale giraffa!
'''


Mammiferi:str = ["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili:str = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli:str = ["aquila", "pappagallo", "gufo", "falco"]
Pesci:str = ["squalo", "trota", "salmone", "carpa"]


print("digita un animale")
a:str = (str(input()))

match a:
    case a if a in Mammiferi:
        print(a + " appartiene alla categoria dei mammiferi")
    case a if a in Rettili:
         print(a + " appartiene alla categoria dei rettili")
    case a if a in Uccelli:
        print(a + " appartiene alla categoria degli uccelli")
    case a if a in Pesci:
        print(a + " appartiene alla categoria dei pesci")
    case _:
        print(a + " non appartiene a nessuna gategoria")
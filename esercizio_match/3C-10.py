'''
Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.
'''

print("digita il giorno")
giorno:int= int(input())          # RICORDA SEMPRE di specificare sia prima nella "definizione" che dopo nell "input" il TIPO di "variabile" 
print("digita il mese")
mese:int= int(input())

data:tuple= (giorno,mese)

match data:
    case (1,1):                                              # RICORDA di usare il "match" sulla "tupla" - le "" o le '' servono solo quando si intendono SINGOLI dati PRECISI
        print(f"Il {giorno}/{mese} è Capodanno!")
    case (14, 2):
        print(f"Il {giorno}/{mese} è San Valentino!")        # con questa annotazione scrivere il "print" è più ottimizato
    case (2, 6):
        print(f"Il {giorno}/{mese} è la Festa della Repubblica Italiana!")     # bisogna mettere le {} attorno alle variabili...
    case (15, 8):
        print(f"Il {giorno}/{mese} è Ferragosto!")
    case (31, 10):
        print(f"Il {giorno}/{mese} è Halloween!")
    case (25, 12):
        print(f"Il {giorno}/{mese} è Natale!")
    case _:
        print(f"Nessuna festività importante in questa data.")

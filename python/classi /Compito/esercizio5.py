'''Esercizio 5
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna.
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''

print("quanti soldi metti nella macchinetta?")
euro = int(input())
contatore = 0
barrette:int = euro
buoni_sconto_rimasti = 0


while True:  
    if euro < 0:   
     break
    else:  
       contatore = (int(euro / 6))                              # calcolo il numero di barrette aggiuntive considerando che 6 buoni corrispondano ad una barretta
       barrette += contatore                                    # "aggiorno" il numero di barrette totali 
       buoni_sconto_rimasti = int((euro - contatore * 6))       # sottraggo il numero di buoni utilizzati rispetto ai buoni totali ( buoni totali = soldi spesi)
    
    print("queste sono le barrette che ottieni ")
    print(str(barrette))
    print("questi sono i tuoi buoni sconto rimasti")
    print(str(buoni_sconto_rimasti))
    break                                                       # il secondo break è fondamentale siccome il ciclo si ripetebbe all'infinito, considerando che la variabile "euro" non varia 
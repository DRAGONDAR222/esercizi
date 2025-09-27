'''In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato #1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.'''


import random

def mossa_tartaruga(posizione):
    n_casuale = random.randint(1, 10)
    if 1 <= n_casuale <= 5:
        posizione = min(70, posizione + 3)  # Passo veloce
        mossa = "Passo veloce (+3)"
    elif 6 <= n_casuale <= 7:
        posizione = max(1, posizione - 6)  # Scivolata
        mossa = "Scivolata (-6)"
    else:
        posizione = min(70, posizione + 1)  # Passo lento
        mossa = "Passo lento (+1)"
    return posizione, mossa

def mossa_lepre(posizione):
    n_casuale = random.randint(1, 10)
    if 1 <= n_casuale <= 2:
        mossa = "Riposo (0)"
    elif 3 <= n_casuale <= 4:
        posizione = min(70, posizione + 9)  # Grande balzo
        mossa = "Grande balzo (+9)"
    elif n_casuale == 5:
        posizione = max(1, posizione - 12)  # Grande scivolata
        mossa = "Grande scivolata (-12)"
    elif 6 <= n_casuale <= 8:
        posizione = min(70, posizione + 1)  # Piccolo balzo
        mossa = "Piccolo balzo (+1)"
    else:
        posizione = max(1, posizione - 2)  # Piccola scivolata
        mossa = "Piccola scivolata (-2)"
    return posizione, mossa

def visualizza_pista(tartaruga, lepre):  # le "funzioni" mossa() riescono a visualizzare le "variabili" tartaruga e lepre (nonostante appartengano che appartengono alla "funzione" gara()) poichè vengono richiamate nella "funzione" in cui sono state inizializzate                   
    pista = ['_'] * 70  # Inizializza la pista con tutti trattini
    if tartaruga == lepre:
        pista[tartaruga - 1] = 'OUCH!!!'  # dato che la "lista" è composta da 70 "elementi" risultano POSIZIONI da 0 a 69
    else:
        pista[tartaruga - 1] = 'T'
        pista[lepre - 1] = 'H'
    
    # Costruire la rappresentazione della pista manualmente con un ciclo for
    rappresentazione = ""   # "stringa" (iniziale) vuota
    for elemento in pista:
        rappresentazione += elemento  # Concatenazione manuale dei caratteri (aggiorna "rappresentazione")
    return rappresentazione   # RAPPRESENTAZIONE è una "stringa" composta da ogni singolo "elemento" della "lista" (aggiunti attraverso il "for")


def gara():
    tick:int = 1
    tartaruga:int = 1
    lepre:int = 1
    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while tartaruga < 70 and lepre < 70:

        print(tick)
        tick+=1
        # Muovere la tartaruga e la lepre
        tartaruga, mossa_t = mossa_tartaruga(tartaruga)  # qui aggiorno le 2 "variabili" con le 2 "variabili" DEL "return"
        lepre, mossa_h = mossa_lepre(lepre)
        
        # Mostrare la pista
        pista = visualizza_pista(tartaruga, lepre)
        print(pista)  # Stampa della pista con trattini
        
        # Stampare le mosse
        print(f"Tartaruga: {mossa_t} | Lepre: {mossa_h}\n")
        
        # Controllare il vincitore
        if tartaruga >= 70 and lepre >= 70:
            print("IT'S A TIE")
            break
        elif tartaruga >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif lepre >= 70:
            print("HARE WINS || YUCH!!!")
            break

# Avviare la gara
gara()
        

    
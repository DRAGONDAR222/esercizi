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

count:int = 0
my_list:list[str,int] = ['T','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']
lepre:int = 0
tartaruga:int = 0

def mossa_tartaruga(n_casuale):
    n_casuale = random.randint(1, 10)

    if 1 <= n_casuale <= 5:
        my_list[tartaruga] = '_'
        tartaruga +=3
        if tartaruga >70:
            tartaruga = 70
        my_list[tartaruga] = 'T'
        mossa: str ="passo veloce"
        return mossa

    if 6 <= n_casuale <= 7:
        my_list[tartaruga] = '_'
        tartaruga -= 6
        if tartaruga <0:
            tartaruga = 0
        my_list[tartaruga] = 'T'
        mossa: str ="scivolata"
        return mossa

    if 8 <= n_casuale <= 10:
        my_list[tartaruga] = '_'
        tartaruga += 1
        if tartaruga >70:
            tartaruga = 70
        my_list[tartaruga] = 'T'
        mossa: str ="passo lento"
        return mossa
    

def mossa_lepre(n_casuale):
    n_casuale = random.randint(1, 10)

    if 1 <= n_casuale <= 2:
        my_list[lepre] = '_'
        lepre += 0
        my_list[lepre] = 'H'
        mossa:str = "riposo"
        return mossa
    
    if 3 <= n_casuale <= 4:
        my_list[lepre] = '_'
        lepre += 9
        if lepre >70:
            lepre = 70
        my_list[lepre] = 'H'
        mossa:str = "grande balzo"
        return mossa
    
    if n_casuale == 5:
        my_list[lepre] = '_'
        lepre -=12
        if lepre <0:
            lepre = 0
        my_list[lepre] = 'H'
        mossa:str = "grande scivolata"
        return mossa
    
    if 6 <= n_casuale <= 8:
        my_list[lepre] = '_'
        lepre += 1
        if lepre >70:
            lepre = 70
        my_list[lepre] = 'H'
        mossa:str = "piccolo balzo"
        return mossa
    
    if 9 <= n_casuale <= 10:
        my_list[lepre] = '_'
        lepre -=2
        if lepre <0:
            lepre = 0
        my_list[lepre] = 'H'
        mossa:str = "piccola scivolata"
        return mossa
    
def posizioni():
    posizioneT = my_list.index('T')
    print("la tartaruga è in posizione" + str(posizioneT))
    posizioneH = my_list.index('H')
    print("la lepre è in posizione" + str(posizioneH))
    print(my_list)
    
    
while my_list[69] == '_':
    count +=1
    print("tick n:" + str(count))

    print(mossa_tartaruga())
    print(mossa_lepre())

    print(posizioni())

    if tartaruga == lepre and count != 0:
        my_list[tartaruga] = 'OUCH!!!'

    if tartaruga == lepre and my_list[tartaruga]== 'H':
        print("IT'S A TIE")

    elif my_list[70] == 'T':
        print("TORTOISE WINS! || VAY!!!")
    elif my_list[70] == 'H':
        print("HARE WINS || YUCH!!!")
        

    
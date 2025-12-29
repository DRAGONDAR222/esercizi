'''Mostri Contro Alieni
 
 
Scrivere queste classi all'interno di un file chiamato ReP3_inizialeNome_Cognome. Ad esempio Mario Rossi dovrà scrivere queste classi all'interno del file chiamato ReP3_M_Rossi.
 
ATTENZIONE! Non saranno valutati programmi che generano errori in fase di esecuzione. Si consiglia pertanto
di “mettere sotto commento” le parti di programma che danno errori, in modo da permettere l'esecuzione del resto del programma. 

Definire le seguenti classi con attributi privati:

Creatura con le seguenti proprietà:
- attributi: nome (di tipo stringa, per indicare il nome della creatura)
- metodi: tutti i metodi standard, ovvero __init__, setter, getter e __str__
In particolare:
il metodo setNome() deve fare un controllo se il nome inserito sia una stringa valida. In caso contrario, impostare il nome della creatura con il valore di "Creatura Generica".
il metodo __str__ deve mostrare in output: "Creatura: nome creatura"


Alieno (che eredita da Creatura) con le seguenti proprietà:
- attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:
il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola con un numero intero positivo casuale tra 10000 e 90000.
Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random e usare la funzione randint(a,b) del modulo;
 
il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni con una lista di 15 numeri interi positivi i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ... Usare le list comprehension.
il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.
Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli. Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto: "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".
il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)

Mostro ( che eredita da Creatura) con le seguenti proprietà:
- attributi: urlo_vittoria (di tipo stringa), gemito_sconfitta (di tipo stringa), assalto (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:
il metodo __init__ deve ricevere il nome del mostro, il suo urlo della vittoria ed il suo gemito sconfitta. Inoltre, deve inizializzare assalto.
il metodo setAssalto() (privato) non riceve argomenti in input e deve inizializzare l'attributo assalto con una lista di 15 numeri interi positivi casuali tra 1 e 100, estremi inclusi, tutti diversi tra loro.
i metodi setVittoria(vittoria: str) e setSconfitta(sconfitta: str) (privati), devono controllare se i valori di vittoria e sconfitta siano valori validi. In caso contrario, devono impostare gli attributi urlo_vittoria a "GRAAAHHH" e gemito sconfitta a "Uuurghhh".
ad esempio, se il nome del mostro è "Godzilla", il metodo __str__ dovrà mostrare a schermo: Mostro: gOdZiLlA, ovvero il nome del mostro scritto con i caratteri alternati minuscolo-maiuscolo.


All'interno del file ReP3_inizialeNome_Cognome (fuori dalla classi) definire le seguenti funzioni:
pariUguali(a: list[int], b: list[int]). Questo metodo riceve in input due liste a e b di interi positivi e deve restituire una lista c.
Ogni elementi della lista c deve essere uguale a:
- 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
- 0 altrimenti

combattimento(a: Alieno, m: Mostro). Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto della classe Mostro. Il metodo deve controllare la validità di a e la validità di m. Se a non è un Alieno o se m non è un Mostro, il combattimento deve essere interrotto, mostrare un opportuno messaggio e ritornare None. Altrimenti, se a e m sono oggetti validi, il metodo deve simulare il combattimento tra Mostro e Alieno, restituendo la creatura vincitrice. Il combattimento consiste nell'applicare la funzione pariUguali() alle munizioni dell'Alieno e all'assalto del Mostro. Se la lista prodotta in output dal pariUguali() ha più di 4 elementi con valore 1, allora il vincitore è il mostro. Altrimenti, il vincitore è l'alieno. Se vince il mostro, sullo schermo viene stampato per 3 volte l'urlo della vittoria, altrimenti viene stampato il gemito della sconfitta.

proclamaVincitore(c: Creatura). Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri ( a seconda dell'oggetto c) e , mostra il vincitore all'interno di un rettangolo con contorno di * come nell'esempio.

*****************************

*                                         *

*    Alieno: Robot-25855    *

*                                         *

*****************************

*************************

*                                   *

*    Mostro: gOrThOr    *

*                                    *

*************************

Suggerimento: stampare prima il rettangolo vuoto, le cui dimensioni sono altezza 5 e lunghezza = lunghezza di c.__str__() + 10
poi, modificare il codice in questo modo:
quando si arriva alla riga centrale del rettangolo (ovvero i=2), si deve stampare il nome del vincitore al centro del rettangolo.
per far questo si deve imporre la condizione i=2 e j =5. Se la condizione è verificata, stampare la creatura c (print(c), end=""), stampare 5 spazi vuoti e un * (print(     *), end="") e poi interrompere l'iterazione corrente.


Infine,
Scrivere nel metodo main, un codice Python che
- Inizializza un mostro e un alieno e stampa i dati corrispondenti sullo schermo.
- Esegue un combattimento tra i due oggetti creati.
- Proclama il vincitore.


Esempio di Output:

Alieno: Robot-41119
Munizioni: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]


Mostro: gOrThOr
Assalto: [13, 23, 28, 80, 50, 56, 33, 55, 15, 20, 15, 94, 42, 16, 46]

Combattimento

GRAAAHHH
GRAAAHHH
GRAAAHHH


I Mostri hanno vinto!

*************************

*                                    *

*    Mostro: gOrThOr    *

*                                    *

*************************'''

import random
import re


class Creatura:
    _nome:str
    _lista_nomi_usati:list[str] = []
    
    def set_nome(self,nome:str) -> None:
        if nome not in self._lista_nomi_usati:
            self._nome = nome
            self._lista_nomi_usati.append(nome)
        else:
            self._nome = "Creatura Generica"

    def get_nome(self) -> str:
        return self._nome
    
    def __init__(self,nome:str) -> None:
         self.set_nome(nome)

    def __str__(self) -> str:
        return f"Creatura: {self.get_nome()}"
    


class Alieno(Creatura):
    _matricola: int
    _munizioni: list[int]

    def _set_matricola(self) -> None:
        self._matricola = random.randint(10000 ,90000)

    def _set_munizioni(self) -> None:
            self._munizioni = [x ** 2 for x in range(0,15)]

    def get_matricola(self) -> int:
        return self._matricola
    
    def get_munizioni(self) -> list[int]:
        return self._munizioni
    
    def __init__(self, nome) -> None:
        self._set_matricola()
        self._set_munizioni()  
        
        if not re.fullmatch(rf"Robot-{self._matricola}",nome):
            nome_alieno:str = f"Robot-{self._matricola}"
            super().__init__(nome_alieno)
            raise ValueError("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
        else: 
            super().__init__(nome)
    
    def __str__(self) -> str:
        return f"Alieno:{self.get_nome}"
    


class Mostro(Creatura):
    
    _urlo_vittoria:str
    _gemito_sconfitta:str
    _assalto:list[int]

    def __init__(self,nome:str,urlo:str,gemito:str):
        self.set_nome(nome)
        self._urlo_vittoria = urlo
        self._gemito_sconfitta = gemito
        self._assalto = self._set_assalto()

    def _set_assalto(self) -> None:
        set_assalto:set[int] = set()
        while len(set_assalto) != 15:
            a:int = random.randint(1,100)
            set_assalto.add(a)
        return list(set_assalto)

    def _set_vittoria(self,vittoria: str) -> None:
        if not isinstance(vittoria,str):
            self._urlo_vittoria = "GRAAAHHH"
    
    def _set_sconfitta(self,sconfitta:str) -> None:
        if not isinstance(sconfitta,str):
            self._gemito_sconfitta = "Uuurghhh"

    def get_assalto(self) -> list[int]:
        return self._assalto
    
    def get_vittoria(self) -> str:
        return self._urlo_vittoria
    
    def get_sconfitta(self) -> str:
        return self._gemito_sconfitta

    def __str__(self) -> str: 
        nome_alternato = ""
        i = 0  
        for c in self.get_nome():
            if i % 2 == 0:
                nome_alternato += c.lower()
            else:
                nome_alternato += c.upper()
            i += 1

        return f"Mostro:{nome_alternato}"



def pariUguali(a: list[int], b: list[int]) -> list[int]:
    c:list[int] = []
    i:int = 0
    for elemento in a:
        if elemento % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
        i += 1
    return c

_vincitore:Creatura 

def combattimento(a: Alieno, m: Mostro) -> None:
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print(f"il combattimento deve essere interrotto")
        return None
    esito:list[int] = pariUguali(a.get_munizioni(), m.get_assalto())
    vittoria_mostro:int = 0
    vittoria_alieno:int = 0
    for elemento in esito:
        if elemento == 1:
            vittoria_mostro += 1
        else:
            vittoria_alieno += 1
    if vittoria_mostro > 4:
        _vincitore = m
        print(m.get_vittoria())
        print(m.get_vittoria())
        print(m.get_vittoria())
    else:
        _vincitore = a
        print(m.get_sconfitta())

def proclamaVincitore(c: Creatura) -> None:
    if c == _vincitore:
        # outer for
        for i in range(5):
            # inner for
            for j in range(len(c.__str__() + 10)):

                # il lato a e il lato d del rettangolo
                if i == 0 or i == 5-1:
                    print("*",end=" ")
                # il lato b e il lato c del rettangolo
                elif j == 0 or j == len(c.__str__() + 10) -1:
                    print("*", end =" ")
                # spazi bianchi
                else:
                    print(" ", end = " ")
            print("\n", end= "")

            
        



'''Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.
Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() per impostare il testo. Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.

Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.
Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
Da: alice@example.com, A: bob@example.com
Titolo: Incontro
Messaggio: Ciao Bob, possiamo incontrarci domani?
 
Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
 
Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
Percorso: nomePercorso/document.txt
Contenuto: Questo e' il contenuto del file.

### Test tramite codice driver:
Creazione degli oggetti:

    Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo del messaggio.
    File: Viene creato un oggetto File specificando il percorso di un file esistente.

Prova dei metodi:

    Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email utilizzando il metodo getText().
    Stampa del testo del file: Viene stampato il contenuto del file utilizzando il metodo getText().

Scrittura del contenuto dell'email su un file:

    Scrittura su file: Il contenuto dell'email viene scritto su un nuovo file chiamato email1.txt utilizzando il metodo writeToFile().

Verifica della presenza di parole chiave:

    Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' è presente nel testo dell'email. Il risultato atteso è True.
    File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' è presente nel testo del file. Il risultato atteso è False.

'''

import re

class Document():

    _testo:str 

    def __init__(self,testo:str) -> None:
        self._testo = self.setText(testo)

    def getText(self) -> str:
        return self._testo
    
    def setText(self,testo:str) -> None:
        self._testo = testo

    def isInText(self,parola:str) -> bool:
        if re.search(rf"{parola}",self._testo):
            return True
        return False
            

class Email(Document):
    _mittente:str
    _destinatario:str
    _titolo:str

    def getMittente(self) -> str:
        return self._mittente
    
    def getDestinatario(self) -> str:
        return self._destinatario
    
    def getTitolo(self) -> str:
        return self._titolo
    
    def setMittente(self,mittente:str) -> None:
        self._mittente = mittente

    def setDestinatario(self,destinatario:str) -> None:
        self._destinatario = destinatario

    def setTitolo(self,titolo:str) -> None:
        self._titolo = titolo


    def __init__(self, corpo:str, mittente:str,destinatario:str,titolo:str) -> None:
        self._mittente = self.getMittente(mittente)
        self._destinatario = self.getDestinatario(destinatario)
        self._titolo = self.getTitolo(titolo)

        super().__init__(corpo)

    def getText(self) -> str:
        return f"Da: {self.getMittente()} A: {self.getDestinatario()}\nTitolo:{self.getTitolo()}\nMessaggio: {self._testo}"
    

    def writeToFile(self) -> None:

        with open('/home/its/Scaricati/programmi - esercizi/recupero/test_esercizio_files/document.txt','w') as file:  # 'a' fa l'append(), 'w' sovrascrive

            file.write(self.getText())

class File(Document):

    _nomePercorso = '/home/its/Scaricati/programmi - esercizi/recupero/test_esercizio_files'


    def leggiTestoDaFile(self,file)
        
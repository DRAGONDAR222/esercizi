'''
# Codificatori Messaggio
Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà sostituita da 'f' e così via.

     Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.

    Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).


Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

    Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al metodo sposta_carattere().

    Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al metodo combinazione().


Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.
'''

from abc import ABC,abstractmethod
from cifrario import *


class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self,testoCodificato:str) -> str:
        pass

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self,testoInChiaro: str) -> str:
        pass


class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):

    _chiave:int

    def __init__(self,chiave:int) -> None:
        self._chiave = chiave

    def codifica(self,testoInChiaro) -> str:
        return caesar_cypher_encrypt(testoInChiaro, self._chiave)
    
    def decodifica(self,testoCodificato):
        return caesar_cypher_decrypt(testoCodificato, self._chiave)

class CifratoreACombinazione(CodificatoreMessaggio,DecodificatoreMessaggio):
    _n:int

    def __init__(self, n:int):
        self._n = n
        

    def _combinazione(self, testo: str) -> str:
        metà = (len(testo) + 1) // 2  
        prima_metà = testo[:metà]
        seconda_metà = testo[metà:]
        
        testo_combinato = ""
        
        for i in range(len(seconda_metà)):
            testo_combinato += prima_metà[i]
            testo_combinato += seconda_metà[i]
        
        if len(prima_metà) > len(seconda_metà):
            testo_combinato += prima_metà[-1]
        
        return testo_combinato

    
    def codifica(self,TestoInChiaro:str) -> str:
        count:int = 0

        while count < self._n:
            count += 1
            TestoInChiaro = self._combinazione(TestoInChiaro)
        
        return TestoInChiaro


    def decodifica(self,testo:str) -> str:
        count:int = 0

        while count < self._n:
            count += 1
            testo = self._decombinazione(testo)

        return testo
        
    def _decombinazione(self,testo:str) -> str:
        prima_metà: str = ""
        seconda_metà:str = ""
        

        for j in range(len(testo)):
            if j % 2 == 0:
                prima_metà += testo[j] 
            else:
                seconda_metà += testo[j]
            
        testo = prima_metà + seconda_metà

        return testo



with open ('/home/its/programmi_esercizi/file/codificatore_read.txt','r') as file:
    text:str = file.read()

if __name__ == '__main__':
    contenuto: str = ""

    # Test Cifratore a Scorrimento
    contenuto += "=== Test Cifratore a Scorrimento ===\n"
    print("=== Test Cifratore a Scorrimento ===")

    chiave = 3
    cifratore_s = CifratoreAScorrimento(chiave)

    contenuto += f"Testo in chiaro letto: {text}\n"
    print("Testo in chiaro letto:", text)

    testo_codificato_s = cifratore_s.codifica(text)
    contenuto += f"Testo codificato: {testo_codificato_s}\n"
    print("Testo codificato:", testo_codificato_s)

    testo_decodificato_s = cifratore_s.decodifica(testo_codificato_s)
    contenuto += f"Testo decodificato: {testo_decodificato_s}\n\n"
    print("Testo decodificato:", testo_decodificato_s)
    print()

    # Test Cifratore a Combinazione
    contenuto += "=== Test Cifratore a Combinazione ===\n"
    print("=== Test Cifratore a Combinazione ===")

    n = 3
    cifratore_c = CifratoreACombinazione(n)

    contenuto += f"Testo in chiaro letto: {text}\n"
    print("Testo in chiaro letto:", text)

    testo_codificato_c = cifratore_c.codifica(text)
    contenuto += f"Testo codificato: {testo_codificato_c}\n"
    print("Testo codificato:", testo_codificato_c)

    testo_decodificato_c = cifratore_c.decodifica(testo_codificato_c)
    contenuto += f"Testo decodificato: {testo_decodificato_c}\n"
    print("Testo decodificato:", testo_decodificato_c)

    # Riscrivi tutto il contenuto nel file
    with open('/home/its/programmi_esercizi/file/codificatore_write.txt', 'w', encoding='utf-8') as file:
        file.write(contenuto)
    
            


        
        
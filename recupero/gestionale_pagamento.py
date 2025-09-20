'''1. GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321'''

from datetime import date

class Pagamento:
    
    __importo: float

    def __init__(self):
        self.__importo = 0.00

    def setImporto(self, importo: float) -> None:
        self.__importo = importo

    def getImporto(self) -> float:
        return self.__importo
    
    def dettagliPagamento(self) -> None:
        print(f'Importo del pagamento: €{self.getImporto():.2f}')


class PagamentoContanti(Pagamento):

    def dettagliPagamento(self) -> None:
        print(f'Pagamento in contanti di: €{self.getImporto():.2f}')

    def inPezziDa(self) -> None:
        importo: float = round(self.getImporto(), 2)

        dict_banconote: dict[int, int] = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0}
        dict_monete: dict[float, int] = {2:0, 1:0, 0.50:0, 0.20:0, 0.10:0, 0.05:0, 0.01:0}

        messaggio_finale: str = f'{importo:.2f} euro da pagare in contanti con:\n'

        for chiave in dict_banconote:
            count = int(importo // chiave)
            if count > 0:
                dict_banconote[chiave] = count
                importo = round(importo - count * chiave, 2)

        for chiave in dict_monete:
            count = int(importo // chiave)
            if count > 0:
                dict_monete[chiave] = count
                importo = round(importo - count * chiave, 2)


        for chiave in dict_banconote:
            if dict_banconote[chiave] > 0:
                messaggio_finale += f'{dict_banconote[chiave]} banconot{"e" if dict_banconote[chiave] > 1 else "a"} da {chiave} euro\n'

        for chiave in dict_monete:
            if dict_monete[chiave] > 0:
                messaggio_finale += f'{dict_monete[chiave]} monet{"e" if dict_monete[chiave] > 1 else "a"} da {chiave:.2f} euro\n'

        print(messaggio_finale)


class PagamentoCartaDiCredito(Pagamento):
    
    __titolare: str
    __scadenza: str
    __num_carta: str

    def __init__(self, titolare: str, scadenza: str, num_carta: str):
        super().__init__()
        self.__titolare = titolare
        self.__scadenza = scadenza
        self.__num_carta = num_carta

    def dettagliPagamento(self):
        print(
            f'Pagamento di: €{self.getImporto():.2f} effettuato con la carta di credito\n'
            f'Nome sulla carta: {self.__titolare}\n'
            f'Data di scadenza: {self.__scadenza}\n'
            f'Numero della carta: {self.__num_carta}'
        )



if __name__ == "__main__":
    # Pagamenti contanti
    p1 = PagamentoContanti()
    p1.setImporto(150)
    p1.dettagliPagamento()
    p1.inPezziDa()

    p2 = PagamentoContanti()
    p2.setImporto(95.25)
    p2.dettagliPagamento()
    p2.inPezziDa()

    # Pagamenti carta di credito
    c1 = PagamentoCartaDiCredito("Mario Rossi", "12/24", "1234567890123456")
    c1.setImporto(200)
    c1.dettagliPagamento()

    c2 = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", "6543210987654321")
    c2.setImporto(500)
    c2.dettagliPagamento()

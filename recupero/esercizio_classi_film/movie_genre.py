from film import Film


    
class Azione(Film):

    __genere:str
    __penale:float


    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = 'Azione'
        self.__penale = 3


    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale

    def calcolaPenaleRitardo(self,giorni:int) -> float:
        return (giorni * self.getPenale())
    

class Commedia(Film):

    __genere:str
    __penale:float


    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = 'Commedia'
        self.__penale = 2.50


    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale

    def calcolaPenaleRitardo(self,giorni:int) -> float:
        return (giorni * self.getPenale())
    
class Drama(Film):

    __genere:str
    __penale:float


    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = 'Drama'
        self.__penale = 2


    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale

    def calcolaPenaleRitardo(self,giorni:int) -> float:
        return (giorni * self.getPenale())
    


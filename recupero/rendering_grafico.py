from abc import abstractmethod,ABC


class Forma(ABC):

    __nome:str

    @abstractmethod
    def __init__(self,nome:str):
        pass 


    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass


class Quadrato(Forma):

    __lato:int

    def __init__(self,lato:int):
        self.__lato = lato
        self.__nome = 'Quadrato'

    def getArea(self):
        return self.__lato ** 2
    
    def render(self):
        for i in range(self.__lato):
            if i == 0 or i == self.__lato - 1:  
                print('*' * self.__lato)
            else:  
                print('*' + ' ' * (self.__lato - 2) + '*')

            
class Rettangolo(Forma):

    __base:int
    __altezza:int

    def __init__(self,base:int,altezza:int):
        self.__nome = 'Rettangolo'
        self.__base = base
        self.__altezza = altezza

    def getArea(self):
        return self.__base * self.__altezza
    
    def render(self):
        for i in range(self.__altezza):
            if i == 0 or i == self.__altezza -1:
                print('*' * self.__base)
            else:
                print('*' + ' ' * (self.__base -2) + '*')


class Triangolo(Forma):
    
    __lato:int

    def __init__(self,lato:int):
        self.__nome = 'Triangolo'
        self.__lato = lato
        
    def getArea(self):
        return (self.__lato ** 2) // 2
    
    def render(self):
        for i in range(self.__lato):
            if i == 0:
                print('*')
            elif i == self.__lato - 1:
                print('*' * self.__lato)
            else:
                print('*' + ' ' * (i - 1) + '*')


r = Triangolo(4)

r.render()




                
        


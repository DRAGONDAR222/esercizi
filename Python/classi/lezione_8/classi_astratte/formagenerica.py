from abc import ABC, abstractmethod


class FormaGenerica(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass


    def setShape(self, shape:str) -> None:
        if shape:
            self.shape = shape
        else:
            print("Errore! la shape non pu├▓ esserer una stringa vuota")

    def getShape(self) -> str:
        return self.shape

class Persona:
    def __init__(self,nome:str,cognome:str,età:int):
        self.setNomePersona(nome) 
        self.setCognomePersona(cognome)
        self.setEtàPersona(età)

    def setNomePersona(self,nome:str) -> None:
        self.nome = nome 

    def setCognomePersona(self,cognome:str) -> None:
        self.cognome = cognome

    def setEtàPersona(self,età:int) -> None:
        if età < 0 or età > 130:
            self.età = 0
        else:
            self.età = età

    def getNomePersona(self) -> str:

        return self.nome
    
    def getCognomePersona(self) -> str:

        return self.cognome
    
    def getEtàPersona(self) -> int:

        return self.età
        
        


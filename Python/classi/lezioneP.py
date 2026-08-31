class Persona:
    def __init__(self,nome:str,cognome:str,et├á:int):
        self.setNomePersona(nome) 
        self.setCognomePersona(cognome)
        self.setEt├áPersona(et├á)

    def setNomePersona(self,nome:str) -> None:
        self.nome = nome 

    def setCognomePersona(self,cognome:str) -> None:
        self.cognome = cognome

    def setEt├áPersona(self,et├á:int) -> None:
        if et├á < 0 or et├á > 130:
            self.et├á = 0
        else:
            self.et├á = et├á

    def getNomePersona(self) -> str:

        return self.nome
    
    def getCognomePersona(self) -> str:

        return self.cognome
    
    def getEt├áPersona(self) -> int:

        return self.et├á
        
        


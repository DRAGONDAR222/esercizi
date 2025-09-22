class Alieno:

    '''
    di un alieno ci serve sapere la galassia di provenoenza 
    self.galaxy: str

    '''

    # inizializzazione di un ogetto della classe Alieno
    def __init__(self,galaxy:str):

        self.setGalaxy(galaxy)
    
    def setGalaxy(self,galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! la galassia di provenienza deve essere una stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy
        
    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}\n"
    
    def speak(self) -> None:
        print("afohheSIF")
        
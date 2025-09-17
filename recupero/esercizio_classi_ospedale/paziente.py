from persona import Persona

class Paziente(Persona):
    __idCode: str

    def __init__(self, first_name: str, last_name: str, idCode: str):
        super().__init__(first_name, last_name)
        self.setIdCode(idCode)

    def setIdCode(self, idCode: str):
        if isinstance(idCode, str):
            self.__idCode = idCode
        else:
            print("Il codice identificativo deve essere una stringa!")
            self.__idCode = None

    def getIdCode(self):
        return self.__idCode

    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()}\nID: {self.__idCode}")
  
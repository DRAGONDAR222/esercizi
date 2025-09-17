from persona import Persona

class Dottore(Persona):
    __specialization: str
    __parcel: float

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        super().__init__(first_name, last_name)
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    def setSpecialization(self, specialization: str):
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
            self.__specialization = None

    def setParcel(self, parcel: float):
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")
            self.__parcel = None

    def getSpecialization(self):
        return self.__specialization

    def getParcel(self):
        return self.__parcel

    def isAValidDoctor(self):
        if self.getAge() is not None and self.getAge() > 30:
            print(f"Doctor {self.getName()} {self.getLastName()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastName()} is not valid!")
            return False

    def doctorGreet(self):
        super().greet()
        print(f"Sono un medico {self.__specialization}")

from dottore import Dottore
from paziente import Paziente

class Fattura:
    __fatture: int
    __salary: float
    __doctor: Dottore
    __patients: list

    def __init__(self, patients: list[Paziente], doctor: Dottore):
        if doctor.isAValidDoctor():
            self.__patients = patients
            self.__doctor = doctor
            self.__fatture = len(patients)
            self.__salary = 0
        else:
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
            self.__patients = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None

    def getSalary(self):
        self.__salary = self.__doctor.getParcel() * self.getFatture()
        return self.__salary

    def getFatture(self):
        self.__fatture = len(self.__patients)
        return self.__fatture

    def addPatient(self, newPatient: Paziente):
        self.__patients.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")

    def removePatient(self, idCode: str):
        for paziente in self.__patients:
            if paziente.getIdCode() == idCode:
                self.__patients.remove(paziente)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato rimosso il paziente {idCode}")
                return paziente
        return None

class Persona:
    def __init__(self):
        self.name:str = ""
        self.lastname:str = ""
        self.age:int = 0

# funzione che mostri i dati relativi ad una persona
    def displayData(self) -> None:
        print(f"nome: {self.name}\ncognome: {self.lastname}\netà: {self.age}")

# funzione che mi consenta di impostare il valore self.name 
    def setName(self, name:str) -> None:
        self.name = name
    
# funzione che mi consenta di impostare il valore self.lastname
    def setLastName(self, lastname:str) -> None:
        self.lastname = lastname
    
# funzione che mi consenta di impostare il valore self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age 

# funzione che mi consenta di ritornare il valore di self.name
    def getName(self) -> str:
        return self.name
    
# funzione che mi consenta di ritornare il valore di self.lastname
    def getlastname(self) -> str:
        return self.lastname
    
# funzione che mi consenta di ritornare l'età della persona 
    def getAge(self) -> int:
        return self.age
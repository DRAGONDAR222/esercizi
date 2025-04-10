'''
from persona import Persona

# creo una persona 
dm:Persona = Persona("Dario","Montuoro",19)

print(dm)

print(dm.name,dm.lastname,dm.age)

# richiamare la funzione dispalyData della classe Persona per mostrare in output i dati relativi alla persona dm
dm.displayData()
'''

# dal file persona2 importa la classe Persona
from persona2 import Persona

dm:Persona = Persona()

# richiamo la funzione displayData della classe Persona per mostrare in output le informazioni relative all'oggetto dm
dm.displayData()

# modificare il nome della persona dm
dm.setName("Dario")

# modificare il cognome della persona dm
dm.setLastName("Montuoro")

# modificare l'età della persona dm
dm.setAge(19)

print("------------------")

dm.displayData()

print("------------------")
print(dm.getName(), dm.getlastname(), dm.getAge())
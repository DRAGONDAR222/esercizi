from persona2 import Persona
from alieno import Alieno


# creare un oggetto p della classe Persona
p: Persona = Persona("Federico","March",29)

# visualizziamo le informazioni della Persona p
print(p)

# creare un oggetto et della Classe Alieno
et: Alieno = Alieno("Andromeda")

# visualizziamo le informazioni dell'Alieno et
print(et)

# l'oggetto invoca il metodo pesak()
p.speak()

# l'oggetto et si prosta ad invocare il metodo speak()
et.speak()


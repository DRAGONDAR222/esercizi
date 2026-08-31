from lezioneP import Persona
from lezioneStudente import Studente

# creare un oggetto p di classe perspona 
p: Persona = Persona("Federico", "March", 29)

# visualizzo le informazioni relative alla persona p
print(p)

# creare un oggetto studente di classe studente
studente1: Studente = Studente("Mario","Rossi",33,"7788")

# volgio controllare che studente1 sia istanza della classe studente
if isinstance(studente1, Studente):
    print("\nstudente ├¿ un oggetto della classe Studente")

# la funzione isinstance(obj, Class) > True se l'oggetto ├¿ un istanza della classe Class

# volgio sapere se studente1 sia anche istanza della classe Persona dato che la classe Studente eredita dalla classe Persona

if isinstance(studente1,Persona):
    print("\nl'oggerro studente1 ├¿ anche un'istanza della classe Persona")
else:
    print("\nl'oggetto studente1 ├¿ solo un'istanza dellla classe Studente e non della classe Pesrona")

# volgio controllare che l'oggetto p sia istanza di Persona
if isinstance(p, Persona):
    print("\nl'oggetto p ├¿ un'istanza della classe Persona")

# voglio controllare se l'oggetto p ├¿ anche istanza della classe Studente
if isinstance(p, Studente):
    print("\nl'oggetto p ├¿ istanza della classe Persona ed ├¿ anche istanza della classe Studente")
else:
    print("\nl'oggetto p ├¿ solo istanza della classe Persona, ma non ├¿ istanza della classe Studente")

# voglio controllare se Studente ├¿ sottoclasse della classe Persona
# issubClass(Class1,Class2)-> controllare se Class1 ├¿ sotttoclasse della classe Classe2 -> in caso affermativo ritona True
if issubclass(Studente,Persona):
    print("\nla Classe Studente ├¿ sottoclasse della classe Persona")

print(studente1)

print(p)

print(f"\nLa media dei voti relativi agli esami sostenuti dallo studente1 ├¿: {studente1.getMediaEsami[10, 20, 30]} ")

# creiamo uno studente2, oggetto della classe Studente
studente2:Studente = Studente(p.getNomePersona(), p.getCognomePersona(), p.getEt├áPersona(), "28394563")

print(studente2)

#confrontare se studente1 == p
print("\n",studente1 == p)

# confronto studente1 e studente2
print("\n", studente1 == studente2)

# verifichiamo che lo studente1 sia = a se stesso
print("\n", studente1 == studente1)

# modificare nome, cognome ed et├á dello studente2 affinch├¿ abbia stesso nome, cognome ed et├á dello studente1
studente2.setNomePersona(studente1.getNomePersona())
studente2.setCognomePersona(studente1.getCognomePersona())
studente2.setEt├áPersona(studente1.getEt├áPersona())

# confronto sudente1 con studente2
print("\n", studente1 == studente2)

# ho forzzato la metricola dello studente2 ad essere uguale alla matricola dello studente1
studente2.setMatricola(studente1.getMatricola())

# confronto se studente1 == studente2
print("\n", studente1 == studente2)


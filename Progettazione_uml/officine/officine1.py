from abc import ABC, abstractmethod
from datetime import date

codici_già_usati:set = set()

class Persona(ABC):

    def __new__(cls, nome: str, cf: str, indirizzo: 'Indirizzo', cell: int, extra):
        if cf not in codici_già_usati:
            codici_già_usati.add(cf)
            if isinstance(extra, int):
                return Dipendente(nome, cf, indirizzo, cell, extra)
            elif isinstance(extra, date):
                return Direttore(nome, cf, indirizzo, cell, extra)
            elif isinstance(extra, Veicolo):
                return Proprietario(nome, cf, indirizzo, cell, extra)
        else:
            print("Immetti correttamente i dati per Persona")
            return None


        
    def __init__(self, nome:str,cf:str,indirizzo:'Indirizzo',cell:int):
        self.nome:str = nome
        self.cf:str = cf
        self.indirizzo:'Indirizzo' = indirizzo
        self.cell:int = cell
    
    def __eq__(self, other):
        if isinstance(other,Persona):
            return self.cf == other.cf  
        return False
        
class Indirizzo:
    pass

class Dipendente(Persona):

    def __init__(self, nome, cf, indirizzo, cell,*args):
        self.anni_servizio:int = args[0]
        self.officina:'Officina' = None
        super().__init__(nome, cf, indirizzo, cell)

class Direttore(Persona):

    def __init__(self, nome, cf, indirizzo, cell,*args):
        self.data_nascita:date = args[0]
        self.officina:'Officina' = None
        super().__init__(nome, cf, indirizzo, cell)

class Proprietario(Persona):
    def __init__(self, nome, cf, indirizzo, cell,veicolo_iniziale:'Veicolo'):
        self.veicoli:list[Veicolo] = [veicolo_iniziale]
        super().__init__(nome, cf, indirizzo, cell)
    
    def assegna(self,veicolo_da_assegnare:'Veicolo'):
        self.veicoli.append(veicolo_da_assegnare)

targhe_già_usate:set = set()

class Veicolo:
    def __new__(cls, modello: str, tipo: str, targa: str, anno_I: int, proprietario: 'Proprietario'):
        if targa not in targhe_già_usate and isinstance(proprietario, Proprietario):
            targhe_già_usate.add(targa)
            return super().__new__(cls)
        else:
            print("Immetti correttamente i dati per Veicolo")
            return None

        
    def __init__(self,modello:str,tipo:str,targa:str,anno_I:int,proprietario:'Proprietario'):
        self.modello:str = modello
        self.tipo:str = tipo
        self.targa:str = targa
        self.anno_I:int = anno_I
        self.proprietari:list['Proprietario'] = [proprietario]
        proprietario.assegna(self)

    def __eq__(self, other):
        if isinstance(other,Veicolo):
            return self.targa == other.targa 
        return False

class Officina:
    def __init__(self,nome:str,indirizzo:'Indirizzo'):
        self.nome:str = nome
        self.indirizzo:'Indirizzo' = indirizzo
        self.dipendenti:list['Dipendente'] = []
        self.direttore:'Direttore' = None
    
    def add_dipendente(self,dipendente_da_aggiungere:'Dipendente'):
        if dipendente_da_aggiungere not in self.dipendenti:
            self.dipendenti.append(dipendente_da_aggiungere)
            dipendente_da_aggiungere.officina = self
        
    def add_direttore(self,direttore_da_aggiungere:'Direttore'):
            self.direttore = direttore_da_aggiungere
            direttore_da_aggiungere.officina = self
    
    def get_n_dipendenti(self):
        return len(self.dipendenti)

class Riparazione(ABC):
    def __new__(cls, *args):
        if len(args) == 7:
            if isinstance(args[5], date) and isinstance(args[6], int):
                return Terminata(*args)
        elif len(args) == 5:
            return In_corso(*args)
        print("Immetti correttamente i dati per Riparazione")
        return None

    def __init__(self, codice: str, data_A: date, ora_A: int, sede: 'Officina', veicolo_da_riparare: 'Veicolo'):
        self.codice: str = codice
        self.data_A: date = data_A
        self.ora_A: int = ora_A
        self.sede: 'Officina' = sede
        self.veicolo_da_riparare: 'Veicolo' = veicolo_da_riparare

class Terminata(Riparazione):
    def __init__(self, codice, data_A, ora_A, sede, veicolo_da_riparare, data_C: date, ora_C: int):
        self.data_C: date = data_C
        self.ora_C: int = ora_C
        super().__init__(codice, data_A, ora_A, sede, veicolo_da_riparare)

class In_corso(Riparazione):
    def __init__(self, codice, data_A, ora_A, sede, veicolo_da_riparare):
        super().__init__(codice, data_A, ora_A, sede, veicolo_da_riparare)

        






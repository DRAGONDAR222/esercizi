from my_tipes.my_general_tipes import *
from my_tipes.custom_types import *
from __future__ import annotations

class Persona:
    _nome:str
    _cognome:str
    _cf:CodiceFiscale
    _data_nascita:date # <<imm>>
    _maternità:IntGEZ | None
    _is_uomo:bool
    _is_donna:bool
    _posizione_militare:StrEnum | None

    def get_nome(self) -> str:
        return self._nome

    def get_cognome(self) -> str:
        return self._cognome
    
    def get_cf(self) -> CodiceFiscale:
        return self._cf
    
    def get_data_nascita(self) -> date:
        return self._data_nascita
    
    def get_maternità(self) -> IntGEZ:
        if not self.get_is_donna():
            raise ValueError("non era una donna")
        return self._maternità
    
    def get_is_uomo(self) -> bool:
        return self._is_uomo
    
    def get_is_donna(self) -> bool:
        return self._is_donna
    
    def get_posizione_militare(self) -> StrEnum:
        if not self.get_is_uomo():
            raise ValueError("non era un uomo")
        return self._posizione_militare
    

    def set_nome(self,nome:str) -> None:
        self.get_nome() = nome

    def set_cognome(self,cognome:str) -> None:
        self.get_cognome() = cognome

    def set_cf(self,cf:CodiceFiscale) -> None:
        self.get_cf() = cf

    def set_maternità(self,maternità:IntGEZ | None) -> None:
        if self.get_is_donna() == True and self.get_maternità() != None:
            self.get_maternità() = maternità
        else: 
            raise ValueError("la persona non è  donna")
        
    def set_is_uomo(self,is_uomo:bool) -> None:
        if is_uomo == True:
            self.get_is_uomo() = is_uomo
        else: 
            self.get_is_uomo() = is_uomo 
            self.get_posizione_militare() = None

    def set_is_donna(self,is_donna:bool) -> None:
        self.get_is_donna() = is_donna

    def set_posizione_militare(self,posizione_militare:StrEnum | None) -> None:
        self.set_is_uomo(True)
        self.get_posizione_militare() = posizione_militare


    def __init__(self,nome:str,cognome:str,cf:CodiceFiscale,nascita:date,maternità:IntGEZ | None = None,posizione_militare:StrEnum | None = None) -> None:
        
        self._data_nascita = nascita
        self._nome = nome
        self._cognome = cognome
        self._cf = cf

        self._is_donna = False
        self._is_uomo = False
        self._maternità = maternità
        self._posizione_militare = posizione_militare
        

        if maternità is not None:
            self._is_donna = True

        if posizione_militare is not None:
            self._is_uomo = True

        if not self.get_is_donna() or self.get_is_uomo:
            raise ValueError("l'individuo deve avere almeno un genere")
        


    def remove_donna(self) -> None:
        if not self.get_is_donna():
            raise ValueError("non era una donnna")
        if not self.get_is_uomo():
            raise ValueError("l'individuo deve avere almeno un genere")
        self.get_maternità() = None
        self.get_is_donna() = False

    def remove_uomo(self) -> None:
        if not self.get_is_uomo():
            raise ValueError("non era un uomo")
        if not self.get_is_donna():
            raise ValueError("l'individuo deve avere almeno un genere")
        self.get_posizione_militare() = None
        self.get_is_uomo() = False



class Impiegato(Persona):
    _ruolo: Ruolo
    _stipendio: FloatGEZ

    def __init__(self, nome, cognome, cf, nascita, ruolo:Ruolo, stipendio: FloatGEZ, maternità = None, posizione_militare = None):
        self._stipendio = stipendio
        self._ruolo = ruolo
        super().__init__(nome, cognome, cf, nascita, maternità, posizione_militare)


class Studente(Persona):
    _matricola: IntGEZ

    matricole_usate:set[IntGEZ] = set()


class Progetto:
    _nome:str
    
    



class Ruolo(StrEnum):
    direttore = 'direttore'
    segretario = 'segretario'
    progettista = 'progettista'
    
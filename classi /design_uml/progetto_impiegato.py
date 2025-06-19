from __future__ import annotations
from datetime import *
from abc import classmethod

class Impiegato:

    _data_nascita:date
    _partecipazioni:set[_Partecipa]           #dict[Progetto,_Partecipa]    RICORDA

    def __init__(self, nome:str,cognome:str,data_nascita:date,stipendio:float) ->  None:
        self.nome = nome
        self.cognome = cognome
        self._data_nascita = data_nascita
        self.stipendio = stipendio
        self._partecipazioni = set()

    def get_nome(self) -> str:
        return self.nome
    
    def get_cognome(self) -> str:
        return self.cognome
    
    def get_data(self) -> date:
        return self._data_nascita
    
    def get_stipendio(self) -> float:
        return self.stipendio
    
    def get_partecipazioni(self) ->  set[_Partecipa]:
        return frozenset(self._partecipazioni)
    
    def set_nome(self,nome:str) -> None:
        self.nome = nome
        
    def set_cognome(self,cognome:str) -> None:
        self.cognome = cognome

    def set_stipendio(self,stipendio:float) -> None:
        self.stipendio = stipendio

    def _add_link_partecipa(self, l: _Partecipa) -> None:
        self._partecipazioni.add(l)

    def _remove_link_partecipa(self, l: _Partecipa) -> None:
        self._partecipazioni.remove(l)

    def is_coinvolto(self, progetto: Progetto) -> bool:
         return progetto in self._partecipazioni


class Progetto:

    _partecipazioni:set[_Partecipa]

    def __init__(self,nome:str,budget:float):
        self.nome = nome
        self.budget = budget
        self._partecipazioni = set()

    def get_nome(self) -> str:
        return self.nome
    
    def get_budget(self) -> float:
        return self.budget
    
    def get_partecipazioni(self) ->  set[_Partecipa]:
        return frozenset(self._partecipazioni)
        
    def set_nome(self,nome:str) -> None:
        self.nome = nome

    def set_budget(self,budget:float) -> None:
        self.budget = budget

    def _add_link_partecipa(self, l: _Partecipa) -> None:
        self._partecipazioni.add(l)

    def _remove_link_partecipa(self, l: _Partecipa) -> None:
        self._partecipazioni.remove(l)

        #crea il remove_link


# crea la classe factory per poter eliminare i link: Partecipa       
    
class Factory:

    @classmethod
    def create_link(cls,data:date,impiegato:Impiegato,progetto:Progetto) -> None:
        l:_Partecipa =_Partecipa(data,impiegato,progetto)
        
        # aggiungo le partecipazioni nell' init

    @classmethod
    def delete_link(cls,l:_Partecipa) -> None:
        if l is None:
            raise ValueError("il link non può essere None")
        l.remove_partecipazione()    
        del l


class _Partecipa:
    
    _data_inizio:date
    _impiegato:Impiegato
    _progetto:Progetto

    def __init__(self,data:date,impiegato:Impiegato,progetto:Progetto):
        self._data_inizio = data
        self._impiegato = impiegato
        self._progetto = progetto
        
        if self not in self._impiegato._partecipazioni:
            self.get_impiegato()._add_link_partecipa(self)
        else:
            raise ValueError("l'impiegato già partecipa al progetto")
        
        if self not in self._progetto._partecipazioni:
            self.get_progetto()._add_link_partecipa(self)
        else:
            raise ValueError("il progetto coinvolge già l'impiegato")
        

    def get_data(self) -> date:
        return self._data_inizio
    
    def get_impiegato(self) -> Impiegato:
        return self._impiegato
    
    def get_progetto(self) -> Progetto:
        return self._progetto
        
    def remove_partecipazione(self) -> None:
        if self in self.get_impiegato().get_partecipazioni() and self in self.get_progetto().get_partecipazioni():
            self.get_impiegato()._remove_link_partecipa(self)
            self.get_progetto()._remove_link_partecipa(self)

        # così facendo mi assicuro che il link possa essere reimplementato in futuro 


if __name__ == '__main__':

    alice = Impiegato()
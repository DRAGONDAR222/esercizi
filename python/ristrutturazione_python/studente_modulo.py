from __future__ import annotations
from typing import Any

class Studente:

    _name:str
    _esami: set[_Esame]

    def __init__(self,name:str) -> None:
        self._name = name
        self._esami:set = set()

    def get_name(self) -> str:
        return self._name
    
    # def add_esame(self,esame:_Esame) -> None:
    #     if esame._studente == self and esame not in self._esami:
    #         self._esami.add(esame)
            

    def add_esame_1(self,modulo:Modulo, voto:int) -> None:
        for i in self._esami:
            if i.get_modulo() == modulo:
                raise ValueError("l'esame include un modulo già salvato")

        esame1 = _Esame(voto,self,modulo)
        self._esami.add(esame1)
       
    def remove_esame(self,modulo:Modulo) -> None:
        for i in self._esami:
            if i.get_modulo() == modulo:
                self._esami.remove(i)
                break
        raise ValueError("l'esame non è presente")
        

    def get_esami(self) -> frozenset[_Esame]:
        return frozenset(self._esami)
    
    def media_voti(self) -> float:
        totale:int = 0
        for esame in self._esami:
            totale += esame.get_voto()

        return totale / len(self._esami)


class Modulo:

    _codice:str 

    def __init__(self,codice:str) -> None:
        self._codice = codice
        

    def get_codice(self) -> str:
        return self._codice
    


class _Esame:

    _voto:int
    _studente:Studente
    _modulo: Modulo

    def __init__(self,voto:int, studente:Studente, modulo:Modulo) -> None:
        self._voto = voto
        self._studente = studente
        self._modulo = modulo

    def get_voto(self) -> str:
        return self._voto
    
    def get_studente(self) -> str:
        return self._studente
    
    def get_modulo(self) -> str:
        return self._modulo
    

        
if __name__=='__main__':

    alice = Studente("Alice")

    prog1 = Modulo("prog.1")

    alice.add_esame_1(prog1, 28)
    alice.add_esame_1(prog1, 30)


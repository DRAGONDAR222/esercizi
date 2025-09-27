from tipi_di_dato.IntGEZ1900 import IntGEZ1900
from typing import Any

class CompagniaAerea:
    
    _anno_fondazione: IntGEZ1900 # immutabile

    def __init__(self, name:str, anno_fondazione: Any) -> None:
        self.name:str = name
        self._anno_fondazione = anno_fondazione


    def get_name(self) -> str:
        return self.name
    
    def set_name(self,name:str) -> None:
        if name != self.name:
            self.name = name

    def get_anno_fondazione(self) -> str:
        return self._anno_fondazione
from tipi_di_dato.IntGEZ import IntGEZ
from typing import Any

class Città:

    _name:str # immutabile

    def __init__(self, name:str, population: Any) -> None:
        self._name = name
        self.population:IntGEZ = IntGEZ(population)

    def get_name(self) -> str:
        return self._name
    
    def get_population(self) -> str:
        return str(self.get_population)
    
    def set_population(self, population:Any) -> None:
        if IntGEZ(population) != self.population:
            self.population = population
    
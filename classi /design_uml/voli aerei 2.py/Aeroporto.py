from tipi_di_dato.CodiceAeroporto import CodiceAeroporto

class Aeroporto:

    _codice_aeroporto: CodiceAeroporto   # immutabile

    def __init__(self, name:str, code: str | CodiceAeroporto) -> None:
        self.name = name
        self._codice_aeroporto = CodiceAeroporto(code)

    def get_name(self) -> str:
        return self.name
    
    def get_codice_aeroporto(self) -> str:
        return self._codice_aeroporto
    
    def set_name(self, name:str) -> None:
        self.name = name


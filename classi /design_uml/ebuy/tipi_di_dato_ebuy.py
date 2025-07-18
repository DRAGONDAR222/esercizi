from typing import Self
from enum import StrEnum
import re


class URL(str):
    def __new__(cls, url: str) -> Self:
        url = url.strip()

        if re.fullmatch(r'https?://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}', url):
            return super().__new__(cls, url)

        raise ValueError(f"'{url}' non è un URL valido!")
    

class Condizioni(StrEnum):
    OTTIMO = "Ottimo"
    BUONO = "Buono"
    DISCRETO = "Discreto"
    DA_SISTEMARE = "Da_Sistemare"


class Voto(int):
    pass

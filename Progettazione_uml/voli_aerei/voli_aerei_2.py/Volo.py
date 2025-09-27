from tipi_di_dato.TimeRange import TimeRange
from tipi_di_dato.CodiceVolo import CodiceVolo
from datetime import *

class Volo:

    _codice_volo: CodiceVolo  # immutabile

    def __init__(self, code: str, duration: TimeRange) -> None:
        self._codice_volo = CodiceVolo(code)
        self.duration:TimeRange = duration

    def get_duration(self) -> TimeRange:
        return self.duration
    

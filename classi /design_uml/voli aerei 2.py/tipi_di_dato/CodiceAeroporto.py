from typing import Self
import re

class CodiceAeroporto(str):
    def __new__(cls, code: Self | str) -> Self:
        Acode:str = str(code).upper().strip()

        if not re.fullmatch(r"[A-Z]{3}", Acode):
            raise ValueError(f"{code} deve essere composto da 3 lettere (maiuscole)")
        return super().__new__(cls,Acode)
    
    
        
    

b = CodiceAeroporto("ABC")

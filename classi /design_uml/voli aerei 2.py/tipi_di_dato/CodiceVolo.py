from typing import Self
import re

class CodiceVolo(str):
    def __new__(cls, code: Self | str) -> Self:
        Vcode:str = str(code).upper().strip()

        if not re.fullmatch(r"[A-Z]{2}[0-9]{3}", Vcode):
            raise ValueError(f"{code} deve essere composto da 2 lettere (maiuscole) e da 3 numeri")
        return super().__new__(cls,Vcode)
    

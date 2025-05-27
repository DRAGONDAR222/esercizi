from typing import Self, Any

class IntGEZ(int):
    def __new__(cls, value: Any) -> Self:
        try:
            Ivalue: int = int(value)
        except ValueError:
            raise ValueError(f"{value} deve essere numerico")
        
        if Ivalue < 0:
            raise ValueError(f"{value} deve essere >= 0")

        return super().__new__(cls, Ivalue)  


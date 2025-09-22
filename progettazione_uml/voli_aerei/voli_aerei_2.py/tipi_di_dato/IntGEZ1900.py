from typing import Self, Any

class IntGEZ1900(int):
    def __new__(cls, value: Any) -> Self:
        try:
            Ivalue: int = int(value)
        except ValueError:
            raise ValueError(f"{value} deve essere numerico")
        
        if Ivalue <= 1900:
            raise ValueError(f"{value} deve essere > 1900")

        return super().__new__(cls, Ivalue)  
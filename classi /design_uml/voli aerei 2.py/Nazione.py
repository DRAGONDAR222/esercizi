class Nazione:
    def __init__(self, name:str) -> None:
        self.name:str = name

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name:str) -> None:
        if name != self.name:
            self.name = name
            
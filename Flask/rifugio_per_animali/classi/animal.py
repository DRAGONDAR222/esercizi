from abc import ABC, abstractmethod

class Animal(ABC):
    id:str              # d1, c3
    name:str            # nome
    age_years:int       # anni
    weight_kg:float     # chilogrammi

    def __init__(self, id:str, name:str, age_years:int, weight_kg:float) -> None:
        self.id = id
        self.name = name 
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species(self):      # Specie
        pass

    @abstractmethod
    def daily_food_grams(self):     # Grammi cibo al giorno
        pass

    def info(self) -> dict:
        info_animale:dict = {
            "id":self.id,
            "name":self.name,
            "species":self.species(),
            "age_years":self.age_years,
            "weight_kg":self.weight_kg
        }

        return info_animale
    
    def bmi_like(self) -> float:    # Indice Massa Corporea
        return self.weight_kg / (self.age_years + 1) 
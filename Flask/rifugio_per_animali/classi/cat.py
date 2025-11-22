from .animal import Animal

class Cat(Animal):
    indoor_only:bool        # Vive solo in casa? (True/False)
    favorite_toy:str        # Gioco preferito (palla, topo)

    def __init__(self, id, name, age_years, weight_kg, indoor_only, favorite_toy) -> None:
        super().__init__(id, name, age_years, weight_kg)
        
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self):
        return "cat"
    
    def daily_food_grams(self):
        formula = 100 + self.age_years * 30
        return f"I grammi di cibo al giorno sono: {formula}" 
    
    def info(self):
        base = super().info()

        base["indoor_only"] = self.indoor_only
        base["favorite_toy"] = self.favorite_toy
        
        return base
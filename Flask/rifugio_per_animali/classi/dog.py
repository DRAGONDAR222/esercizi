from .animal import Animal

class Dog(Animal):
    breed:str           # Razza (Labrador)
    is_trained:bool     # Addestrato? (True/False)

    def __init__(self, id, name, age_years, weight_kg, breed, is_trained) -> None:
        super().__init__(id, name, age_years, weight_kg)
        
        self.breed = breed
        self.is_trained = is_trained

    def species(self):
        return "dog"
    
    def daily_food_grams(self):
        formula = 200 + self.age_years * 50
        return f"I grammi di cibo al giorno sono: {formula}" 
    
    def info(self):
        base = super().info()

        base["breed"] = self.breed
        base["is_trained"] = self.is_trained
        
        return base
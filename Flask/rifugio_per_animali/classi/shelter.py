from .animal import Animal
from .cat import Cat
from .dog import Dog

class Shelter:  # contenitore di tutti gli animali
    animals:dict[str, Animal]
    adoptions:dict

    def __init__(self):
        self.animals = {}
        self.adoptions = {}

    def add(self, animal:Animal):
        if animal.id not in self.animals:
            self.animals[animal.id] = animal
        else:
            print(f"Attenzione: L'animale con ID {animal.id} è già presente.")

    def get(self, animal_id):
        return self.animals.get(animal_id)
    
    def list_all(self) -> list[Animal]:
        lista_animali:list = []

        for animal in self.animals.values():
            lista_animali.append(animal)

        return lista_animali
    
    def is_adopted(self, animal_id) -> bool:
        return animal_id in self.adoptions
    
    def set_adopted(self, animal_id, adopter_name):
        self.adoptions[animal_id] = adopter_name
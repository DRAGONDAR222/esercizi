'''
1. Create an abstract class Person:
Attributes:

name
age
Methods:

get_role, an abstract method to be implemented by subclasses.
__str__, method to return a string representation of the person.
'''

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @abstractmethod
    def get_role(self) -> None:
        pass

    def __str__(self) -> str:
        return f'Name: {self._name} - Age: {self._age}'
        

        


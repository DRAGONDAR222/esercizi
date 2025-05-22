'''Exercise 1: Creating an Abstract Class with Abstract Methods
Start by defining an abstract base class called Shape. This class should include two abstract methods: one named area, which will be responsible for calculating the area of a shape, and another named perimeter, which will calculate the perimeter. Since Shape is abstract, it will not provide specific implementations for these methods. Instead, it sets a blueprint for all shapes that will inherit from it.

Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class. Each of these subclasses must provide their own implementation of the area and perimeter methods, based on the geometric formulas appropriate to their shapes.

Finally, write a simple driver program (test code) that creates instances of Circle and Rectangle, calls their area and perimeter methods, and prints the results. This will help verify that your class hierarchy works as intended.'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass

    @abstractmethod
    def perimeter(self) -> int:
        pass

class Circle(Shape):
    def __init__(self, raggio: int):
        self.raggio:int = raggio

    def area(self) -> int:
        return int(math.pi * self.raggio ** 2)

    def perimeter(self) -> int:
        return int(2 * math.pi * self.raggio)

class Rectangle(Shape):
    def __init__(self, larghezza: int, altezza: int):
        self.larghezza:int = larghezza
        self.altezza:int = altezza

    def area(self) -> int:
        return self.larghezza * self.altezza

    def perimeter(self) -> int:
        return 2 * (self.larghezza + self.altezza)

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle: Area = {circle.area()}, Perimeter = {circle.perimeter()}")
print(f"Rectangle: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}")



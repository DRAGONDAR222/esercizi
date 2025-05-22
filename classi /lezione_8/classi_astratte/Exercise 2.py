'''Exercise 2: Implementing Static Methods
Create a class called MathOperations to group together some basic arithmetic functionality. Inside this class, define two static methods:

add, which accepts two numeric parameters and returns their sum.

multiply, which also takes two numeric parameters and returns their product.

Finally, write a small driver program to test the functionality of the add and multiply methods. This should involve calling both methods with sample inputs and printing the results to verify that they work correctly.'''

class MathOperations:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

# Programma di test
somma = MathOperations.add(5, 3)
prodotto = MathOperations.multiply(5, 3)

print(f"Somma: {somma}")
print(f"Prodotto: {prodotto}")

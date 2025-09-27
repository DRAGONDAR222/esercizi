'''9-13. Dice: Make a class Dice with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
 Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

import random

class Dice:
    def __init__(self, sides: int = 6):  # Imposto sides con un valore predefinito di 6
        self.sides = sides

    def roll_die(self):
        n_casuale = random.randint(1, self.sides)  # Uso self.sides per specificare le facce del dado
        print(n_casuale)


print("6-Sided Die Rolls:")
dice6 = Dice()                       # non specifico il numero di facce 
for elemento in range(10):
    dice6.roll_die()


print("10-Sided Die Rolls:")
dice10 = Dice(10)
for elemento in range(10):
    dice10.roll_die()


print("20-Sided Die Rolls:")
dice20 = Dice(20)
for elemento in range(10):
    dice20.roll_die()



        
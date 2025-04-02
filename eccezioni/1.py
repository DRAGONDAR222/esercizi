'''Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message.'''

import math

def safe_sqrt(number:int):
    try:
        return (math.sqrt(number))
        
    except ValueError:
        return (f"the number should not be negative")


print(safe_sqrt(-4))
print(safe_sqrt(7))
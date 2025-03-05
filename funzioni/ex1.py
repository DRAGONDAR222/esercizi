'''Exercise 1
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.'''

num:int 

def check_value(num):
    if num > 5:
        print(num + "is bigger than 5")
    elif num < 5:
        print(num + "is smaller than 5") 
    else:
        print(num + "is equal to 5") 
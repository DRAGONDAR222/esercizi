'''Exercise 4
Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.'''


num_list:int[list]

def check_each(num_list):
    for elemento in num_list:
        if elemento > 5:
            print(elemento + "is bigger than 5")
        elif elemento < 5:
            print(elemento + "is smaller than 5") 
        else:
            print(elemento + "is equal to 5") 
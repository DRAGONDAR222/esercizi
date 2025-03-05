'''Exercise 2
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

word:str 

def check_lenght(word): 
    if len(word) > 10:
        print(word + "is bigger then 10 characters")
    if len(word)< 10:
        print(word + "is smaller then 10 characters")
    else:
        print(word + "is equal to 10 characters")   
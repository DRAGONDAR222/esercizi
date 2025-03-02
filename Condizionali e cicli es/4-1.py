'''4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!'''



my_list:str = []

print("digit 3 kinds of pizzas which you like the most")

while len(my_list) < 3:
    a:str = input(str())
    my_list.append(a) 


for elemento in my_list:
    print( "i like " + elemento + " pizza")

print(" I really love pizza!")
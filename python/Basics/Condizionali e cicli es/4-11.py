'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list.
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.'''



my_list:str = []

print("digit 3 kinds of pizzas which you like the most")

while len(my_list) < 3:
    a:str = input(str())
    my_list.append(a) 


for elemento in my_list:
    print( "i like " + elemento + " pizza")

print(" I really love pizza!")

friend_pizzas:str = my_list.copy()                # il "metodo" .copy()  serve a copiare tutti gli elementi, ponendo 2 "liste" come uguali (es:a = b) il programma non creerà 2 liste separate bensì assoggetterà un nuovo nome alla lista originale

print("add a new pizza to the origial list")
a:str = input(str())
my_list.append(a)

print("add a new pizza to the new list")
a:str = input(str())
friend_pizzas.append(a)

for elemento in my_list:
    print(str(elemento))

for elemento in friend_pizzas:
    print(str(elemento))
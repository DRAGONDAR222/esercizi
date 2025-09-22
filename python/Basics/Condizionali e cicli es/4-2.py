'''4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!'''


my_list:str = []

print("digit 3 kinds of animals which have one common characteristic ")

while len(my_list) < 3:
    a:str = input(str())
    my_list.append(a) 

for elemento in my_list:
    print( "A " + elemento + " would be a great pet")

print("Any of these animals would make a great pet!")
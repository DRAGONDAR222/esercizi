'''3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''


print("i can invite only 2 people for dinner")

my_friends_lyst = ['Alfredo', 'Giancarlo', 'Martina', 'Carlo', 'Irene', 'Simone']

print("i'm sorry that i can't invite you " + my_friends_lyst[0])     # così facendo pur considerando sempre l'elemento in posizione 0 questo sarà sempre diverso
my_friends_lyst.pop(0)                                               # poichè ogni volta sostituito
print("i'm sorry that i can't invite you " + my_friends_lyst[0])
my_friends_lyst.pop(0)
print("i'm sorry that i can't invite you " + my_friends_lyst[0])
my_friends_lyst.pop(0)
print("i'm sorry that i can't invite you " + my_friends_lyst[0])
my_friends_lyst.pop(0)

print(my_friends_lyst[0] + " you're still invited")
print(my_friends_lyst[1] + " you're still invited")

del my_friends_lyst         # cancello la mia lista 
print(my_friends_lyst)

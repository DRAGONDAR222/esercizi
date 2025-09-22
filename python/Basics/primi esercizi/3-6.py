'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''


my_friends = ["Martina","Carlo","Simone"]

print("shall we have a dinner today " + my_friends[0])
print("shall we have a dinner today " + my_friends[1])
print("shall we have a dinner today " + my_friends[-1])

print("call:" + " i've found a bigger table")

my_friends.insert(0,"Alfredo")
my_friends.insert(1,"Giancarlo")
my_friends.insert(-1,"Irene")

print("shall we have a dinner today " + my_friends[0])
print("shall we have a dinner today " + my_friends[1])
print("shall we have a dinner today " + my_friends[2])
print("shall we have a dinner today " + my_friends[3])
print("shall we have a dinner today " + my_friends[4])
print("shall we have a dinner today " + my_friends[5])


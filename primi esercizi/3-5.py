'''3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''


my_friends = ["Vincenzo","Carlo","Simone"]

print("shall we have a dinner today " + my_friends[0])
print("shall we have a dinner today " + my_friends[1])
print("shall we have a dinner today " + my_friends[-1])    # si può usare anche la ricerca per posizione inversa

print("call " + my_friends[0])

my_friends.insert(0,"Martina")          # inserisco in posizione 0 martina

my_friends.remove("Vincenzo")           # escludo specificatamente l'elemento Vincenzo

print("shall we have a dinner today " + my_friends[0])
print("shall we have a dinner today " + my_friends[1])
print("shall we have a dinner today " + my_friends[-1])
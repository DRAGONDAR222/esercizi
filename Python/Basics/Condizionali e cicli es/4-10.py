'''4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.'''


# l'esercizio da cui prendo riferimento è il 4-7


my_list:int = []

for i in range(3,34,3):  # passo da "31" a "34" per avere 3 numeri nel mezzo (la lista così diventerebbe dispari)
    my_list.append(i)

print(str(my_list))
                                                                    # la funzione "slice" si traduce in [:n] dove n indica l'argomento (quantitativo) di numeri da stampare, che essendo tra [] va ad indicare l'indice
print("The first three items in the list are: " + str(my_list[:3])) # scrivendo ":3" tra [] io sottolineo che devo scrivere i numeri dalla posizione "0" dell' INDICE alla poisizione "3" col "3" ESCLUSO: posizione(0,1,2) 

print("Three items from the middle of the list are: " + str(my_list[4:7]))     # dall' indice "4" all'indice "7" con "4" incluso ed "7" escluso                            

print("The last three items in the list are: " + str(my_list[-3:]))  # n: indica da dove devo iniziare, mettre :n dove deve arrivare (non avendo scpecificato nulla dopo i : lo "slice" ha una posizione specifica di "arrivo" e considera tutti gli elementi)
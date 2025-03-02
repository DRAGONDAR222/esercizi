'''4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)'''

my_list:int = []

for i in range(1,1000000,1):
    my_list.append(i)

print(str(my_list))    # il "print" posto duori dal mio cliclo mi permette di stampare DIRETTAMENTE la mia lista completa
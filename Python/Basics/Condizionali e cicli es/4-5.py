'''4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers'''


my_list:int = []

for i in range(1,1000001,1): # "mettendo "1000001" faccio la somma icludendo tutto il milione intero escluso l' 1 finale
    my_list.append(i)

print(int(min(my_list)))
print(int(max(my_list)))
print(int(sum(my_list)))

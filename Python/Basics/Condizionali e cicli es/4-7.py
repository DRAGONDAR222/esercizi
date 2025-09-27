'''4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.'''


my_list:int = []

for i in range(3,31,3):
    my_list.append(i)

print(str(my_list))
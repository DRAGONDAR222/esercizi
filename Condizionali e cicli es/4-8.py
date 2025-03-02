'''4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.'''



my_list:int = []

for i in range(1,11,1):
    a:int = i**3         # "a" è una variabile che corrisponde al "cubo" di "i" che viene AGGIORNATA ad ogni ciclo 
    my_list.append(a)

print(str(my_list))
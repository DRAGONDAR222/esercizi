'''Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.
Expected Output:
Sum of integers from 1 to 10 is 55
Sum of integers from 20 to 37 is 513
Sum of integers from 35 to 49 is 630'''


sum1:int = 0
sum2:int = 0
sum3:int = 0

for i in range(1, 11): # "i" sta per "numero" - il punto d'arrivo deve essere "n+1" per CONSIDERARE ogni ciclo desiderato
    sum1 += i
print(" sum from 1 to 10 is:" + str(sum1))

for i in range(20, 38):
    sum2 += i
print(" sum from 20 to 37 is:" + str(sum2))

for i in range(35, 50):
    sum3 += i
print(" sum from 35 to 50 is:" + str(sum3))
'''1-4. Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

2
0
2
4'''

print(int(2024/1000))   # avendo messo "int" il programma esclude la parte decimale del numero
n =(int(2024%1000))     # cosnidero i numeri a sinistra del 2
print(int(n/100))       # l'int esclude i decimali e ci mostra soltanto le centinaia 
n = (int(2024%100))
print(int(n/10))
n = (int(2024%10))
print(int(n/1))









print(int(2124%1000))   # il % serve ad indicare tutti i numeri restanti (a sinistra) dopo l'ultimo numero divisible per intero, utilizzando il numero di percentuale es: 124
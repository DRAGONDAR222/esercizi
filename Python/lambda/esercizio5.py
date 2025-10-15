'''Esercizio 5 – Funzione lambda con if
Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".'''

verifica_pari:str = lambda x: print("pari") if x %2==0 else print("dispari")

verifica_pari(3)

verifica_pari(4)
'''`Scrivere un programma PYTHON che a partire da una stringa la cifra con la tecnica XOR
Successivamente mostrare che la stringa cifrata, riapplicando lo stesso XOR, torna la stringa originale
Per fare lo XOR utilizzate un solo valore: 57
Quindi data la stringa di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni carattere della stringa lo xor con il valore 57
“N” xor 57, “e” xor 57, …
Ottenendo una lista di numeri es: 78 (che è il codice asciii  della lettera N) xor (si indica con il simbolo ^) => 78 ^ 57 = 119
E così via per tutta la stringa.
Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 57 e quindi ottenere (ricostruendola) la stringa originale
NB: potreste utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia il valore segreto da applicare come xor
`'''

# stringa:str = 'Nel mezzo del cammin di nostra vita'

# stringa_hash:list = [ord(i) for i in stringa]

# stringa_xor:list = [i ^ 57 for i in stringa_hash]

# print(stringa_xor)

# stringa_not_xor:list = [i ^ 57 for i in stringa_xor]

# stringa_not_hash:list = [chr(i) for i in stringa_not_xor]

# stringa_ricostruita:str = ""

# for i in stringa_not_hash:
#     stringa_ricostruita += i

# print(stringa_ricostruita)


def codifica(stringa:str,xor:int) -> list[int]:
    stringa_hash:list[int] = [ord(i) for i in stringa]

    stringa_xor:list[int] = [i ^ xor for i in stringa_hash]

    print(stringa_xor)
    return stringa_xor



def decodifica(stringa_xor:list[int],xor:int) -> str:
    stringa_not_xor:list = [i ^ xor for i in stringa_xor]

    stringa_not_hash:list = [chr(i) for i in stringa_not_xor]

    stringa_ricostruita:str = ""

    for i in stringa_not_hash:
        stringa_ricostruita += i

    print(stringa_ricostruita) 
    return stringa_ricostruita  



test:list[int] = codifica('Nel mezzo del cammin di nostra vita',57)
decodifica(test,57)


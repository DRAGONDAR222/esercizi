''' 1. Somma dei numeri pari in una lista
Scrivi una funzione che restituisce la somma dei numeri pari presenti in una lista.'''

def somma_pari(lista: list[int]) -> int:
    return sum([x for x in lista if x % 2 == 0])


print(somma_pari([1, 2, 3, 4]))  # ➜ 6


'''2. Conta le vocali in una stringa (case-insensitive)
 Scrivi una funzione che conta quante vocali ci sono in una stringa (ignorando maiuscole/minuscole).'''

def conta_vocali(s:str):
    vocali:str = 'aeiou'

    return len([i for i in s if i.lower() in vocali])
 

print(conta_vocali("Ciao Mondo"))  # Output atteso: 5


''' 3. Crea una "piramide" di asterischi (*)
 Dato un numero n, crea una lista di stringhe che rappresenta una piramide con n righe.'''

def piramide(n: int) -> list[str]:
    return ['*' * i for i in range(1, n + 1)]



'''4. Inverti una lista (senza usare slicing [::-1])
 Scrivi una funzione che restituisce la lista in ordine inverso.'''

def inverti(lista: list[int]) -> list[int]:
    return [lista[i] for i in range(len(lista) - 1, -1, -1)]


print(inverti([1, 2, 3]))  # ➜ [3, 2, 1]


'''5. Verifica se una stringa è palindroma
Scrivi una funzione che restituisce True se una stringa si legge uguale da sinistra a destra e viceversa.'''

def is_palindroma(s: str) -> bool:
    return s == s[::-1]


print(is_palindroma("radar"))  # ➜ True
print(is_palindroma("cane"))   # ➜ False



'''6. Conta le occorrenze delle lettere (escludendo gli spazi)
 Dato un testo, restituisci un dizionario con la frequenza di ogni lettera (senza considerare gli spazi).'''

def conta_lettere(s: str) -> dict:
    s = s.replace(" ", "")  # rimuove gli spazi
    risultato = {}

    for c in s:
        if c in risultato:
            risultato[c] += 1
        else:
            risultato[c] = 1

    return risultato


print(conta_lettere("ciao ciao"))  
# Output: {'c': 2, 'i': 2, 'a': 2, 'o': 2}


'''7. Restituisci il massimo tra tre numeri (senza usare max())
 Ordina i tre numeri in una lista e restituisci l’ultimo elemento (il più grande).'''

def massimo(a: int, b: int, c: int) -> int:
    return sorted([a, b, c])[-1]


print(massimo(3, 8, 5))  # ➜ 8


'''8. Filtra parole lunghe almeno N caratteri
 Dato un elenco di parole, restituisci solo quelle con lunghezza >= n.'''

def filtra_parole(lista: list[str], n: int) -> list[str]:
    return [parola for parola in lista if len(parola) >= n]


print(filtra_parole(["ciao", "a", "mondo"], 4))  # ➜ ['ciao', 'mondo']


'''9. Simula l’output di un if/else
 Data una funzione, prevedi cosa stampa in base all'input.'''

def test(x: int):
    if x % 2 == 0:
        print("Pari")
    else:
        print("Dispari")


test(5)  # ➜ Dispari
test(6)  # ➜ Pari




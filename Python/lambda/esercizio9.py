'''Esercizio 9 – Ritorna una lambda
Scrivi una funzione moltiplicatore(n
) che ritorni una lambda che moltiplica un valore per n.

Esempio d'uso:

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20'''

def moltiplicatore(n:int) -> int:
    moltiplicato:int = lambda x: x * n
    return moltiplicato

per_due = moltiplicatore(2)

print(per_due(10))
'''Nella Sala dell’Equilibrio ogni cifra viene giudicata: oscura, neutra o luminosa. Tieni il verdetto con `sign(n)`: restituisci `-1` se `n` è negativo, `0` se è zero, `1` se è positivo. Mantieni la firma esatta e lascia che i test ti aprano il passaggio.'''

def sign(n: int) -> int:
    

    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1
'''Per aprire la Camera del Vincolo imprigiona una costante in un gesto che allunghi ogni mano che lo invoca: usa `curry_add(n)` per restituire una funzione che sommi `n` al valore ricevuto. Mantieni la firma e soddisfa i test.'''

def curry_add(n):
    def sum_n(x):
        return x + n
    return sum_n
'''Le due sfere ora chiedono ciò che le separa: elementi che vibrano in **una sola** delle due. Evocalo con `symdiff_sorted(a, b)`, restituendo la lista **ordinata** degli interi che compaiono esattamente in una delle liste. Mantieni la firma e placa i test.'''

def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    
    return sorted([x for x in a if x not in b] + [x for x in b if x not in a])
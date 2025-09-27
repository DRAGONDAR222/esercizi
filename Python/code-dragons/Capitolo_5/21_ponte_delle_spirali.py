'''Il Ponte delle Spirali si attiva solo quando sommi i passi del rituale senza saltarne uno: pronuncia `range_sum(n)` per restituire la somma dei numeri da `1` a `n` inclusi; se `n` è minore o uguale a `0`, torna `0`. Mantieni la firma e lascia che i test si aprano come archi luminosi.'''

def range_sum(n: int) -> int:

    if n <= 0:
        return 0
    
    return sum([x for x in range(1,n+1)])
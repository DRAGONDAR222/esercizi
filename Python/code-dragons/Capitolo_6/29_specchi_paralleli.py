'''Tra Specchi Paralleli, l’energia non deve eccedere né mancare. Contienila con `clamp(x, lo, hi)`, restituendo `x` limitato all’intervallo `[lo, hi]`. Mantieni la firma e soddisfa i test.'''

def clamp(x: float, lo: float, hi: float) -> float:
    
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x
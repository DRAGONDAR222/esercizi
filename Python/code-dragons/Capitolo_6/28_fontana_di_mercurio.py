'''Una fontana di mercurio mette alla prova il discernimento: versa soltanto se è sicuro. Realizza `safe_div(a, b, default=None)` restituendo `default` quando `b == 0`, altrimenti `a/b` come **float**. Mantieni la firma e placa i test.'''

def safe_div(a: float, b: float, default=None):
    
    return default if b == 0 else round(a/b,2)


'''Nel Repertorio degli Accordi un tomo ti sfida a trovare sigilli precisi anche quando le pagine sembrano vuote. Evoca `get_or_default(d, k, default)`: restituisci `d[k]` se esiste, altrimenti `default`, senza modificare `d`. Mantieni la firma e accontenta i test come custodi.'''

def get_or_default(d: dict, k, default=None):
    
    return d[k] if k in d else default
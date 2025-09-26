'''Il custode ti affida un bastone da viaggio: raggiungi ogni nodo dell'albero arcano seguendo sentieri annidati, o accetta il silenzio. Cammina con `deep_get(d, path, default)` seguendo chiavi e indici in `path` tra dizionari e liste `d`; restituisci il passo ma, se manca, restituisci `default`. Mantieni la firma e apri i test come portali.'''

def deep_get(d: dict | list, path: list, default=None):
    for step in path:
        if isinstance(d, dict):
            if step in d:
                d = d[step]
            else:
                return default
        elif isinstance(d, list):
            if isinstance(step, int) and 0 <= step < len(d):
                d = d[step]
            else:
                return default
        else:
            return default
    return d

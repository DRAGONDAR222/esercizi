'''I diagrammi intrecciano formule e chiedono un canale dove un incanto scorra dentro l'altro: costruisci `compose(f, g)`, restituendo una funzione che, chiamata con `x`, calcola `g(x)` e poi `f` del risultato. Mantieni la firma e placa i test.'''

def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed
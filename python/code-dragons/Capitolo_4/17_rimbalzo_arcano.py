'''I maestri vogliono che un incanto rimbalzi due volte sullo stesso bersaglio per saggiarne la stabilità: lascialo risuonare con `apply_twice(fn, x)`, applicando `fn` a `x` due volte di seguito e restituendo il risultato finale. Mantieni la firma e soddisfa i test.'''

def apply_twice(fn, x):

    return fn(fn(x))
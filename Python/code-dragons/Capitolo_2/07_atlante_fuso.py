'''Due atlanti rivali scintillano sul leggio: fondi le mappe tenendo solo le rune più recenti. Compila `merge_overwrite(a, b)` per restituire un nuovo dizionario dove i valori di `a` sono sovrascritti dagli aggiornamenti in `b`. Mantieni la firma e appaga i test.'''

def merge_overwrite(a: dict, b: dict) -> dict:

    for chiave,valore in a.items():
        if chiave in b:
            a[chiave] = b[chiave]


    for chiave, valore in b.items():
        if chiave not in a:
            a[chiave] = valore

    return a
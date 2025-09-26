'''Due iscrizioni sembrano reciproci riflessi. Verifica l'incanto con `are_anagrams(a, b)`: ritorna `True` se le due parole/frasi usano le **stesse lettere** al netto degli **spazi** e delle **maiuscole**, altrimenti `False`. Mantieni la firma e soddisfa i test.'''

def are_anagrams(a: str, b: str) -> bool:

    a_lettere:list[str] = [carattere for carattere in a.lower() if carattere.isalpha()]
    b_lettere:list[str] = [carattere for carattere in b.lower() if carattere.isalpha()]
    
    return set(a_lettere) == set(b_lettere)
    
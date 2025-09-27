'''L'ultima sala canta note ripetute: devi comprimerle senza perdere il motivo. Intona `rle(s)` per restituire la codifica run‑length come lista di tuple `(carattere, conteggio)` scorrendo `s`; se `s` è vuota, `[]`. Mantieni la firma e placa i test.'''

def rle(s: str) -> list[tuple[str,int]]:

    if not s:
        return []
    
    my_dict:dict = {}

    for lettera in s:
        if lettera in my_dict:
            my_dict[lettera] += 1
        else:
            my_dict[lettera] = 1

    return[(x,y) for x,y in my_dict.items()]
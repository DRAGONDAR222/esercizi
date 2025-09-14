def pulisci_testo(testo: str) -> str:

    testo_pulito = ''.join([x for x in testo.lower() if x.isalnum() or x == ' '])
   
    return ' '.join(testo_pulito.split())



'''Gli stemmi degli arconti chiedono inversioni fedeli: ogni simbolo ritrovi il proprio portatore. Esegui `invert_unique(d)`, che inverte chiavi e valori assumendo valori univoci. Mantieni la firma e compiaci i test.'''

def invert_unique(d: dict) -> dict:

    my_dict:dict = {}

    for chiave,valore in d.items():
        my_dict[valore] = chiave

    return my_dict
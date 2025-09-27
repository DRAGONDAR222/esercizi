'''Prima di continuare, fonde le fibre raccolte in un'unica trama lineare. Realizza l'intreccio con `flatten_once(nested)`, che appiattisce di un livello una lista di liste concatenando le sottoliste. Mantieni la firma e verifica che i test scorrano senza nodi.'''

def flatten_once(nested: list[list[int]]) -> list[int]:

    if len(nested) == 0:
        return nested

    my_list:list = []
   
    for x in nested:
        my_list += x

    return my_list


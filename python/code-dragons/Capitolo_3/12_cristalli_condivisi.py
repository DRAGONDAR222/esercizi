'''Davanti a due sfere gemelle devi estrarre solo ciò che riecheggia in entrambe. Invoca `intersection_sorted(a, b)` per restituire la lista **ordinata** degli interi presenti sia in `a` sia in `b`, senza duplicati. Mantieni la firma e apri il varco dei test.'''

def intersection_sorted(a: list[int], b: list[int]) -> list[int]:

    my_list:list[int] = []

    for x in a:
        if not x in my_list and x in b:
            my_list.append(x)

    return sorted(my_list)
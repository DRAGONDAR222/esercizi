'''Un tamburo bronzeo batte ritmi di tre e cinque; il varco risponde alla loro somma: evoca `sum_multiples(limit)` per restituire la somma di tutti i numeri **minori di** `limit` divisibili per `3` **oppure** `5`. Se `limit` ≤ `0`, torna `0`. Mantieni la firma e soddisfa i test.'''

def sum_multiples(limit: int) -> int:


    if limit <= 0:
        return 0
    else:
        return sum([x for x in range(0,limit) if x % 3 == 0 or x % 5 == 0])
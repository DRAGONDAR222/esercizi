'''Nel corridoio delle torce, solo quelle pari restano accese insieme: conta quante sono invocando `count_even(nums)`, che restituisce quante voci della lista sono **pari** (incluso `0`). Mantieni la firma e placa i test.'''

def count_even(nums: list[int]) -> int:

    return len([x for x in nums if x % 2 == 0 or x == 0])
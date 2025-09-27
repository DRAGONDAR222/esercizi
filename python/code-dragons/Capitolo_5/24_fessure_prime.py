'''Le mura hanno incavi per gemme **prime**: devi elencarle tutte. Forja `primes_up_to(n)` per restituire la lista dei numeri primi **≤ n** in ordine crescente; se `n` < `2`, ritorna `[]`. Mantieni la firma e apri i test.'''

def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []

    my_list: list[int] = []

    for x in range(2, n + 1):
        is_prime = True
        for j in range(2, int(x ** 0.5) + 1):
            if x % j == 0:
                is_prime = False
                break
        if is_prime:
            my_list.append(x)

    return my_list

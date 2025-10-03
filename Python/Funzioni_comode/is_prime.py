def is_prime(x):
    if x <= 1:
        return False
    
    is_prime = True
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            print(j)
            is_prime = False
            break
    
    return is_prime

print(is_prime(12345678912345678912313111))
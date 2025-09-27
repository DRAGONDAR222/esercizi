'''Al cuore del santuario si snoda il labirinto di Fibonacci: evita di ripetere i passi già tracciati invocando `fib_memo(n)`, che calcola l'ennesimo numero della sequenza con memoria per non rifare i calcoli. Mantieni la firma e lascia che i test si aprano.'''

def fib_memo(n: int, memo={0: 0, 1: 1}) -> int:

    if n in memo:
        return memo[n]
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

    

            
                 


def recursive_Sum(n:int) -> int:
    if n < 0:
        print("errore")
        return None
    elif n == 0:
        return n  # corrisponde a "0"
    else:
        return int(n + recursive_Sum(n-1))
    

print(recursive_Sum(3)) # senza il "print" la "funzione" esegue i calcoli senza rappresentarli in "output"

# 6 (3+2+1)/ (n+(n-1)+(n-2))    

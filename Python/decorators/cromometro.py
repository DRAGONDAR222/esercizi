def cronometro(fun):
    def wrapper(*args):
        import time
        start:float = time.time()
        fun(*args)
        print(time.time() - start)
        # risultato in notazione scientifica

    return wrapper


# ciao = cronometro(ciao)

@cronometro
def ciao():
    print('ciao')

ciao()

@cronometro
def sum_numbers(a:int,b:int):
    print(sum([a,b]))

sum_numbers(1,2)




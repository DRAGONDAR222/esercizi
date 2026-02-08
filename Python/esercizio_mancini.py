# def myfunction(k:int, n:int) -> None
#         Stampa tutte le n-ple di interi tra 1 e k.


#         Per esempio, se invocata come: myfunction(10, 3), allora stampa:

#                                 1  1  1
#                                 1  1  2
#                                 1  1  3
#                                 ...
#                                 1  1 10
                               
#                                 1  2  1
#                                 1  2  2
#                                 1  2  3
#                                 ...
#                                 1  2 10

#                                 1  3  1


def myfunction(k:int, n:int) -> None:                   # (maxValore,lunghezza)
    def aggiungi_numero(n_pla:list[int]) -> None:       # ricorsiva
        if len(n_pla) == n:
            print(n_pla)
            return
        for num in range(1, k+1):
            aggiungi_numero(n_pla + [num])              # unisce le liste fino a creare l'ennupla
    aggiungi_numero([])

myfunction(10,3)


# le varie ennuple derivano dal for che 
# richiama le ricorsive che a loro volta richiamano altri for...

# il fulcro sta nel fatto che ogni passaggio si ramifica
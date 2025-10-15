'''Esercizio 7 – Filtra parole corte
Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"] Estrai solo le parole con più di 4 lettere usando filter() e lambda.'''

parole:list[str] = ["cane", "gatto", "elefante", "ratto", "orso"]

estratte:list[str] = list(filter(lambda x: len(x)>4,parole))

print(estratte)
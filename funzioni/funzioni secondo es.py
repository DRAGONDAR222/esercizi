'''Let’s try to define a function named subtract ourselves:
● It should take 2 parameters.
● Inside the function, it should subtract the two.
● Then, return the result.'''


def substract(a:int,b:int):
    risultato:int = a-b
    return risultato

# "return" è il valore FINALE che viene attribuito come risultato della "funzione" (indipendentemente dai processi avvenuti nella funzione stessa)
# senza il "return" avremmo soltato il PROCESSO senza alcun esito
# utilizzando la "funzione" in qualsiasi "processo" questa corrisponderà direttamente al suo corrispettivo "return" (i processi intermedi è come se avenissero dietro le quinte)
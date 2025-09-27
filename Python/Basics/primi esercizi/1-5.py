'''1-5. Si scriva un programma che converta la temperatura da Fahrenheit a Celsius utilizzando la formula

gradiCelsius=5∗(gradiFahrenheit−32)/9

Si inizializzi una temperatura espressa in gradi Fahrenheit con un numero intero.

La temperatura deve essere convertita e visualizzata in gradi Celsius con un numero in virgola mobile con una precisione di un decimo di grado.

Un possibile esempio di output potrebbe essere il seguente:

72 gradi Fahrenheit corrispondono a 22.2 gradi Celsius.'''


a:int = 72

a:float = (((72-32)/9)*5)
print(a)
a:float = round(a,1)      # round funziona mettendo () prima il numero desiderato, poi il numero preciso di decimali dopo la virgola che si vogliono visualizzare
print(a)
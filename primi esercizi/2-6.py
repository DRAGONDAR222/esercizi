'''2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message. '''

famous_person:str = "Albert Einstein"
quote:str = "“A person who never made a mistake never tried anything new.”"

message = famous_person + " once said:" + quote           #al contrario della parentesi qui non bisogna usare le , ma i +, inoltre per distaccare la prima variabile dal testo occorre digitare uno spazio all'inizio del testo stesso
print(message)
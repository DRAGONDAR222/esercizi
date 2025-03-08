'''8-9. Messages: Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.'''

my_list:list[str]= ["message1","message2","message3"]

def show_messages(my_list):   # qui IMPOSTO l'esito della "funzione"
    for elemento in my_list:
        print(str(elemento))

show_messages(my_list)        # qui la ESEGUO



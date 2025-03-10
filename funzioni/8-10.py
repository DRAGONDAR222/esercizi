'''8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.'''


my_list:list[str]= ["message1","message2","message3"]

def show_message(my_list):
    for elemento in my_list:
        print(str(elemento))

show_message(my_list)

new_list:list[str]=[]

def send_messages(my_list,new_list):
    for elemento in my_list[:]:
        print(str(elemento))
        new_list.append(elemento)
        my_list.remove(elemento)

send_messages(my_list,new_list)

print("Messaggi originali:"+str(my_list))
print("Messaggi inviati:"+ str(new_list))
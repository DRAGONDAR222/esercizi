'''8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.'''


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
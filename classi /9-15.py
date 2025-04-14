'''9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called simulate_until_win(self, my_ticket) that:

Accepts a ticket (a list of 4 items).
Repeatedly draws random tickets using the draw_ticket() method.
Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
Returns the number of attempts and the winning ticket.
2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

Your ticket
The winning ticket
How many attempts it took to win'''


import random

class LotteryMachine:
    def __init__(self, num1:int, num2:int, num3:int, num4:int, num5:int, num6:int, num7:int, num8:int, num9:int, num10:int, let1:str, let2:str, let3:str, let4:str, let5:str):    # così specifico il QUANTITATIVO di lettere e numeri
       
        self.list_items = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, let1, let2, let3, let4, let5]
        
        
    def draw_winning_ticket(self):
        # creo l'attributo "winning_ticket"
        self.winning_ticket = random.sample(self.list_items, 4) # uso la libreria "random" per creare una "lista" coi 4 "elementi" casuali
        return self.winning_ticket

    def display_winning_message(self):
        return f"Any ticket matching the winning 4 items {self.winning_ticket} wins a prize!"
    
    def draw_ticket(self):
        # creo l'attributo "my_ticket"
        self.my_ticket:list = random.sample(self.list_items, 4) # uso la libreria "random" per creare una "lista" coi 4 "elementi" casuali
        return self.my_ticket
    
    def simulate_until_win(self, my_ticket):
        winning_ticket:list = self.draw_winning_ticket()    
        count:int = 1
        while True:
            if my_ticket != winning_ticket:
                print("round " + str(count))
                my_ticket = self.draw_ticket()
                count += 1
            else:
                print(f"it took: {count} rounds to win")
                print(f"this is the winning ticket: {winning_ticket}")
                print(f"this is my ticket: {my_ticket}")
                break
                
                


        

lottery = LotteryMachine(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E') 

my_ticket:list = lottery.draw_ticket()

print(my_ticket)

lottery.simulate_until_win(my_ticket)

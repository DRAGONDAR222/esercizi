'''9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket.
 Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.'''

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


lottery = LotteryMachine(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E') 

winning_ticket = lottery.draw_winning_ticket()

print("Winning ticket:", winning_ticket)

print(lottery.display_winning_message())

        



        
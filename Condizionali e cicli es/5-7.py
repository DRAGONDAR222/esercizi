'''5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!'''


favourite_fruits = ["mango","pear","kiwi"]

if "mango" in favourite_fruits: # "if" al contrario di "elif" permette più casi contemporaneamente
    print("you like mangoes!")
if "apple" in favourite_fruits:
    print("you don't like apples so much")
if "peach" in favourite_fruits:
    print("how dare you!")
if "kiwi" in favourite_fruits:
    print("gg")
if "albero" in favourite_fruits:
    print("incredible!")
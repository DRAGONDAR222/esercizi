'''9-2. Three Restaurants: Start with your class from Exercise 9-1.
Create three different instances from the class, and call describe_restaurant() for each instance.'''

class Restaurant:

    def __init__(self,restaurant_name:str,cuscine_type:str):
        self.restaurant_name = restaurant_name
        self.cuscine_type = cuscine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuscine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


poi_ti_dico = Restaurant("poi","ti dico")
poi_ti_dico.describe_restaurant()                                 # per richiamare uan "funzione dobbiamo srvivere un . dopo il nome della variabile, che sarà a sua volta susseguito dal nome della "funzione" stessa "
# altri 2 esempi...
'''9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. '''

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number: int):
        self.number_served = number                   # sets the number

    def increment_number_served(self, number: int):
        self.number_served += number                  # uptade that number


# Create an instance of Restaurant
restaurant = Restaurant("Trattoria Roma", "Italian")

# Print initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Change the number served and print again
restaurant.number_served = 10
print(f"Number of customers served: {restaurant.number_served}")

# Use set_number_served method
restaurant.set_number_served(20)
print(f"Number of customers served: {restaurant.number_served}")

# Use increment_number_served method
restaurant.increment_number_served(15)
print(f"Number of customers served: {restaurant.number_served}")


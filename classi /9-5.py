'''9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.'''


class User:

    def __init__(self, first_name:str,last_name:str,age:int):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attemps = 0
    
    def describe_user(self):
        print(f"the first name is:{self.first_name}, the last name is: {self.last_name} and the age is: {self.age}")
    
    def greet_user(self):
        print(f"thank you {self.first_name} {self.last_name}")
    
    def increment_login_attempts(self):
        self.login_attemps += 1

    def reset_login_attempts(self):
        self.login_attemps = 0 

    
user = User("Dario","Moccia",23)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"number of login atempts = {user.login_attemps}")

user.reset_login_attempts()

print(f"number of login atempts = {user.login_attemps}")


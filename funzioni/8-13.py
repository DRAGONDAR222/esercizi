'''8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''


print("digit your first and last names")
your_name:str = str(input())
your_surname:str = str(input())

def build_profile(*args):
    print(f"{your_name} {your_surname} ")
    for arg in args:
        print(f"{arg}")

build_profile("age:13","eyes:brown","hair:blonde")
    
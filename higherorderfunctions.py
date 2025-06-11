def greet_louder(name):
    print(f"Hi {name.upper()}")


def greet_softer(name):
    print(f"Hi {name.lower()}")


def display(other_func,name):
    print("your name is ")
    other_func(name)
display(greet_louder,"Roshny")
display(greet_softer,"roShny")
#display is higher order function


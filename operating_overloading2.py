class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __gt__(self, other):
        return self.age > other.age

p1 = Person("Ram", 32)
p2 = Person("Shyam", 23)

if p1 > p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")

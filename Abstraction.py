#main_abstarct.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_types = n

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("Hi I am calling from vehicle class")



#subclasses.py

class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):
        print("Start with kick")

    def display(self):
        print("This is Bike")
class Scooty(Vehicle):
    def __init__(self, n):
        super().__init__(n)

    def start(self):
        print("self start")
class Car(Vehicle):
    def __init__(self, n, x):
        super().__init__(n)
        self.no_of_gears = 6

    def start(self):
        print("start with key")



#call.py

from main import *

bike = Bike(2, "Black")
bike.start()         # Output: "Start with kick"
bike.display()       # Output: "This is Bike"

scooty = Scooty(2)
scooty.start()       # Output: "self start"
scooty.display()     # Output: "Hi I am calling from vehicle class"

class Human:
    def __init__(self, num_heart):
        print("calling init from Human")
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart

    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")

class Male:
    def __init__(self, name):
        print("Calling init from Male")
        self.name = name

    def flirt(self):
        print("I can flirt")
class Boy(Human, Male):
    def __init__(self, name, heart, language):
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.language = language

    def sleep(self):
        print("I can sleep")

    def work(self):  # This overrides Human's 'work' method
        print("I can test")

    def display(self):
        pass  # You can add print statements here to show all attributes if you like
    def work(self):
        print("I can work")
boy_1 = Boy("Rahul", 1, "Python")
print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)

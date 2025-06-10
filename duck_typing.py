class Duck:
    def swim(self):
        print('swim')
    def speaks(self):
        print('quack')
class Dog:
    def swim(self):
        print("dog can swim")
    def speaks(self):
        print('dog can bark')
    def walk(self):
        print('dog can walk')
class Demo():
    def display(self,gen):
        gen.swim()
        gen.speaks()
d=Duck()
dog = Dog()
demo = Demo()
demo.display(dog)
demo.display(d)

#python doent care about the class it only looks for all the methods are defined or not

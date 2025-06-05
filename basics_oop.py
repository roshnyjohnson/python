class Circle:
    pi=3.14
    def __init__(self,r):
        self.radius=r
        self.area=self.pi*r*r
    def circumference(self):
        return 2* self.pi *self.radius
    # def area(self):
    #     return self.pi*self.radius*self.radius
circle_1=Circle(5)
print(circle_1.circumference())
circle_2=Circle(4)
print(circle_2.circumference())
print(circle_1.area)

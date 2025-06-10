class complexnumber():
    def __init__(self, r, i):
        self.real = r
        self.imaginary= i

    def __add__(self,other):
       return  f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
c1=complexnumber(2,7)
c2=complexnumber(6,1)
print(c1+c2)#we are overloading the operation add

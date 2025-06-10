class Student:
    def __init__(self,name,rollno,age):
        print("iam created")
        self.name=name#protected double underscore
        self._rollno=rollno#private double underscore
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
       if age>20:
           print("invalid")
       else:
           self.__age=age

    def __display(self):
        print(f"hi iam {self.name} and my roll no is {self._rollno} my age is{self.__age}i am from student class")
    def displayPrivateData(self):
        self.__display()
class Branch(Student):
    pass
s1=Student("John",66,16)
b1=Branch("roshny",64,18)
s1.displayPrivateData()
##print(s1.__age) gives error
print(b1.name)
print(b1._rollno) #dispalys with underscore usage so better to not use it like that
print(dir(s1))
print(s1._Student__age)#n0 error
print(s1._rollno)
s1._Student__display()
print(s1.get_age())
s1.set_age(12)
print(s1.get_age())

#b1.display()#by default access specifier is public

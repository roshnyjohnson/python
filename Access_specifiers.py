class Student:
    def __init__(self,name):
        print("iam created")
        self.name=name
    def display(self):
        print(f"hi iam {self.name} and i am from student class")
s1=Student("John")
s2=Student("Jane")
s1.display()#by default access specifier is public




#2nd
class Student:
    def __init__(self,name,rollno,age):
        print("iam created")
        self.name=name#protected double underscore
        self._rollno=rollno#private double underscore
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

#b1.display()#by default access specifier is public

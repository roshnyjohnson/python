import my_module as m

print(m.a)
print(m.area_of_square(4))


from my_module import calculaor
calculator(3,2)



my_module.py
a = 10

def area_of_square(side):
    return side ** 2

def calculator(x, y):
    print("Addition is: ", x + y)
    print("Subtraction is: ", x - y)
    print("Multiplication is: ", x * y)
    print("Division is: ", x / y)

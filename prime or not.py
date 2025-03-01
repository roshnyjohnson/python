import math
num=int(input('enter a number'))
if num==0 or num==1:
    print("not prime number")
for i in range(2,math.ceil(num/2)+1):
    if num%i==0:
        print("not prime number")
        break

else:
    print("prime")

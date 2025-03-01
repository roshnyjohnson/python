import math
def paint(height,width,coverage):
    cans=(height*width)/coverage
    print(f"no of cans is { math.ceil(cans) }")
h=int(input("enter height"))
w=int(input("enter width"))
c=int(input("enter the coverage by 1 can"))
paint(h,w,c)

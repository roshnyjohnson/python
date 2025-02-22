in1=input("which pizza do you want to order\na.small(100 rupees)\nb.medium(300 rupees)\nc.large(300 rupees)\nenter a ,b,or c\n")
bill=0
if in1== 'a':
    bill+=100
elif in1=='b':
    bill+=200
elif in1=='c':
    bill+=300
else:
    print("wrong input")
in2=input("do you want peperoni?(Y/N) 30 rupees for small \n50 rupees for medium and large ")
if in2=='y'or in2=='Y':
    if input=='a':
        bill+=30
    else:
        bill+=50
else:
    print("no peperoni ordered")
in3=input("do you want extra cheese('Y/N')\n extra cheese is 20 rupees")
if in3=='y'or in3=='Y':
    bill+=20
else:
    print("no cheese ordered")
print("thankyou for ordering, your bill is",bill)

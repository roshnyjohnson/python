f1=open("file_1.txt","w")
f1.write("welcome iam roshny") #overwrites if something was already present i file_1


f1=open("file_1.txt","r+")
print(f1.read())#file pointer is at the beginning of file
print(f1.tell())
f1.write("hi")
print(f1.tell())#tells the position of filepointer



f1=open("file_1.txt","w+")
print(f1.tell())
f1.write("hello iam roshny")
print(f1.tell())
f1.seek(0)#moves file pointer to beginning
print(f1.tell())
print(f1.read())
print(f1.tell())


f1=open("file_1.txt","a+")
f1.write("hello iam roshny")
print(f1.tell())
f1.seek(0)
print(f1.read())


f1=open("image_1.jpg","rb")
f2=open("image_2.jpg","rb")
for i in f1:
    f2.write(i)

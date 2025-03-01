student_data=[{
    "name":"revathy",
    "roll no":8,
    "age":55,
    "course":"java"
},
{
    "name":"ravi",
    "roll no":6,
    "age":50,
    "course":"c"
}]
def add_new(name,rollno,age,course):
    student={}
    student["name"]=name
    student["roll no"]=rollno
    student["age"]=age
    student["course"]=course
    student_data.append(student)

add_new("shyam",33,4,"C++")
print(student_data)

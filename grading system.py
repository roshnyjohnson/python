student_marks={
    "jenny":92,
    "harry":78,
    "dimpy":56,
    "rahul":41,
    "aniket":99
}
student_grades={}
for i in student_marks:
    marks=student_marks[i]
    if marks>90:
        student_grades[i]="A+"
    elif marks>80:
        student_grades[i] = "A"
    elif marks>70:
        student_grades[i] = "B+"
    elif marks>60:
        student_grades[i]="B"
    elif marks>50:
        student_grades[i]="C"
    elif marks>40:
        student_grades[i]="D"
    else:
        student_grades[i]="F"
print(student_grades)

from turtle import Turtle,Screen
s1=Screen()
tom=Turtle()
tom.shape("turtle")
for i in range(10):

    tom.pendown()
    tom.forward(10)
    tom.penup()
    tom.forward(10)
s1.exitonclick()

# import turtle
# abc=turtle.Turtle()
# xyz=turtle.Turtle() OR

from turtle import Turtle,Screen
s1=Screen()
tom=Turtle()
tom.forward(100)
tom.shape("turtle")
print(tom.pencolor())
# tom.pencolor("red")

# tom.fillcolor("green")
tom.color("blue","yellow")
tom.circle(100)
tom.penup()
tom.forward(100)
tom.pendown()
tom.pensize(100)
print(tom.pos())
tom.penup()
tom.goto(200,200)
print(tom.pos())
tom.pendown()
tom.hideturtle()
tom.circle(50)
s1.exitonclick()

#OR
# from turtle import *
# tom=Turtle()
# forward(100)
# exitonclick()

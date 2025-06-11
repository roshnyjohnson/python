from turtle import Turtle,Screen
import random
s1=Screen()
tom=Turtle()
colors=["red","green","yellow","blue","magenta","cyan"]
tom.shape("turtle")
tom.width(10)
for i in range(50):
    tom.setheading(random.randrange(0,360,90))
    tom.pencolor(random.choice(colors))
    tom.forward(30)
s1.exitonclick()

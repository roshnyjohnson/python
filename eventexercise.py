from turtle import Turtle,Screen

# Create screen and turtle object
screen = Screen()
tom = Turtle()

# Define movement functions
def move_forward():
    tom.forward(100)

def move_backward():
    tom.backward(100)

def turn_left():
    new_heading = tom.heading() + 20
    tom.setheading(new_heading)
    tom.forward(10)

def turn_right():
    new_heading = tom.heading() - 20
    tom.setheading(new_heading)
    tom.forward(10)

def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

# Set up key bindings
screen.listen()
screen.onkey(fun=move_forward, key="f")
screen.onkey(fun=move_backward, key="b")
screen.onkey(fun=turn_left, key="l")
screen.onkey(fun=turn_right, key="r")
screen.onkey(fun=clear_screen, key="c")

# Keep the window open until it is closed by the user
screen.mainloop()

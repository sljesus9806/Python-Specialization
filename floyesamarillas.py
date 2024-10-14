##system that creates a exe file that shows yellow flowers in graphic mode

import turtle
import random

def dibujar_flor():
    #draw the stem
    turtle.color("green")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    
    #draw the petals
    turtle.color("yellow")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(36):
        turtle.forward(50)
        turtle.right(170)
    turtle.end_fill()


#set up the screen

turtle.speed(0)
turtle.bgcolor("purple")

#draw 10 flowers
for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    dibujar_flor()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

#hide the turtle
turtle.hideturtle()
turtle.done()

#------------------------------------------------------------


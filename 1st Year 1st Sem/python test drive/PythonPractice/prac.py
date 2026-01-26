import turtle
import math

def circle(name, radius, resolution):
    name = turtle.Turtle()
    name.speed(50)
    name.pencolor(pen_color)
    name.width(2)

    pi = math.pi

    circumference = 2 * pi * radius
    angle = (((resolution-2)*180)/resolution)+180
    length = circumference/resolution

    resolution = int(resolution)

    for x in range(resolution):
        name.fd(length)
        name.rt(angle)


name = str(input("Circle's Name: "))
resolution = float(input("Resolution (bigger number makes it rounder): "))
radius = float(input("Radius: "))
pen_color = str(input("What color is your circle? "))
circle(name, radius, resolution)
turtle.mainloop()
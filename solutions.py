import turtle
import time
import math


def line():
    t.forward(100)


def circle():
    t.circle(100)


def dashed_line():
    drawing = True

    for i in range(0, 14):
        if drawing:
            t.penup()
        else:
            t.pendown()

        t.forward(20)
        drawing = not drawing


def triangle():
    for i in range(0, 3):
        t.forward(100)
        t.left(120)


def square():
    for i in range(0, 4):
        t.forward(100)
        t.left(90)


def hexagon():
    for i in range(0, 6):
        t.forward(50)
        t.left(60)


def audi():
    for i in range(0, 4):
        t.circle(60)
        t.penup()
        t.forward(80)
        t.pendown()


def olympic_logo():

    for i in range(0, 3):
        t.circle(60)
        t.penup()
        t.forward(130)
        t.pendown()

    t.penup()
    t.left(180)
    t.forward(195 + 130)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.pendown()

    for i in range(0, 2):
        t.circle(60)
        t.penup()
        t.forward(130)
        t.pendown()


def custom_circle():
    for i in range(0, 360):
        t.right(1)
        t.forward(1)


def wave():
    mod = 1
    t.right(90)

    for i in range(0, 6):
        t.circle(40 * mod, 180)
        mod *= -1


def custom_wave():
    for i in range(0, 720):
        t.right(math.cos(math.radians(i)))
        t.forward(1)


def test_all():
    functions = [
        line, circle, dashed_line, triangle, square, hexagon, audi,
        olympic_logo, custom_circle, wave, custom_wave
    ]

    for fun in functions:
        fun()
        time.sleep(1)
        t.reset()
        t.shape('turtle')


if __name__ == '__main__':
    t = turtle.Turtle()
    t.shape('turtle')
    test_all()

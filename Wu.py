import turtle
def heng(x, y, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.down()
    turtle.forward(length)

def shu(x, y, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(-90)
    turtle.down()
    turtle.forward(height)
    
def wangou(x, y, head_angle, radius, circle_angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(head_angle)
    turtle.down()
    turtle.circle(radius, circle_angle)
    turtle.seth(90)
    turtle.forward(50)

def dian(x, y, angle, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(angle)
    turtle.down()
    turtle.forward(length)

def Wumain():
    turtle.setup(600, 600, 200, 200)
    turtle.pensize(20)
    turtle.pencolor("blue")
    heng(-100, 50, 200)
    heng(-200, 0, 400)
    shu(-100, -50, 100)
    shu(0, 0, 150)
    heng(0, -75, 75)
    heng(-150, -150, 250)
    wangou(120, 80, -90, 600, 30)
    dian(160, 65, -45, 50)
    turtle.done()
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
import turtle
def PrintIntro():
    print("这个程序绘制蟒蛇")
    print("这个程序需要输入画笔的大小与颜色")

def Initial(width, hight, x, y):
    turtle.setup(width, hight, x, y)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()

def drawSnake(radius, angle, length):
    turtle.seth(-40)
    for i in range(length):
        turtle.circle(radius, angle)
        turtle.circle(-radius, angle)
    turtle.circle(radius, angle/2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40* 2/3)

def PenSet(size, color):
    turtle.pensize(size)
    turtle.pencolor(color)

def PythonIn():
    temp = input("请分别设置画笔的大小和颜色：")
    Color = temp.strip("0123456789 ")
    Size = eval(temp.replace(temp.strip("0123456789"), ""))
    return Size, Color

def PythonMain():
    PrintIntro()
    Initial(650, 350, 200, 200)
    Size, Color = PythonIn()
    PenSet(Size, Color)
    drawSnake(40, 80, 4)
    turtle.done()
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition

if __name__ == '__main__':
    PythonMain()
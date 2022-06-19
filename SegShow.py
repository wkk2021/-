import turtle
def PrintIntro():
    print("这个程序对所输入内容使用七段数码管显示")
    print("这个程序需要输入所需显示的日期或者十六进制数")

def PenSet():
    turtle.pensize(1)
    turtle.pencolor("blue")

def rst1():
    turtle.penup()
    turtle.right(90)
    turtle.fd(2.5)
    turtle.right(45)
    turtle.fd(50)
    turtle.right(45)
    turtle.fd(2.5)
    turtle.left(45)

def rst2():
    turtle.right(90)
    turtle.fd(6.22)
    turtle.right(45)
    turtle.fd(44.7)
    turtle.right(45)
    turtle.fd(6.22)
    turtle.left(45)
    
def drawGap(): 
    turtle.penup()
    turtle.fd(2.5)

def DrawLine1(draw):
    drawGap()
    PenSet()
    if draw:
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("blue")
        turtle.left(45)
        turtle.fd(2.5)
        turtle.right(45)
        turtle.fd(50)
        turtle.right(45)
        turtle.fd(2.5)
        turtle.right(90)
        turtle.fd(10)
        turtle.right(45)
        turtle.fd(39.37)
        turtle.right(45)
        turtle.fd(10)
        turtle.end_fill()
        rst1()
    else:
        turtle.fd(53.5)
    drawGap()
    turtle.right(90)

def DrawLine2(draw):
    drawGap()
    PenSet()
    if draw:
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("blue")
        turtle.left(45)
        turtle.fd(6.22)
        turtle.right(45)
        turtle.fd(44.7)
        turtle.right(45)
        turtle.fd(6.22)
        turtle.right(90)
        turtle.fd(6.22)
        turtle.right(45)
        turtle.fd(44.7)
        turtle.right(45)
        turtle.fd(6.22)
        turtle.end_fill()
        rst2()
    else:
        turtle.fd(53.5)
    drawGap()
    turtle.right(90)
def DrawDigit(d):
    DrawLine2(True) if d in ['2','3','4','5','6','8','9','A','b','d','E','F'] else DrawLine2(False)
    DrawLine1(True) if d in ['0','1','3','4','5','6','7','8','9','A','b','d'] else DrawLine1(False)
    DrawLine1(True) if d in ['0','2','3','5','6','8','9','b','C','d','E'] else DrawLine1(False)
    DrawLine1(True) if d in ['0','2','6','8','A','b','C','d','E','F'] else DrawLine1(False)
    turtle.left(90)
    DrawLine1(True) if d in ['0','4','5','6','8','9','A','b','C','E','F'] else DrawLine1(False)
    DrawLine1(True) if d in ['0','2','3','5','6','7','8','9','A','C','E','F'] else DrawLine1(False)
    DrawLine1(True) if d in ['0','1','2','3','4','7','8','9','A','d'] else DrawLine1(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) 
def DrawDate(date):
    k = 0
    z = ['年', '月', '日']
    for i in date:
        for j in i:
            DrawDigit(j)
        turtle.pensize(5)
        turtle.write(z[k],font=("Arial", 18, "normal"))
        turtle.pencolor("green")
        turtle.fd(40)
        k = k + 1

def DrawH(H):
    for i in H:
        DrawDigit(i)

def InputDate():
    import re
    Show = input("请输入日期:")
    ShowDate = re.findall("\d+", Show)
    return ShowDate

def InputH():
    ShowH = input("请输入数码管显示十六进制中16个字符的任意组合：")
    j = 0
    for i in ShowH:
        if i in ['0','1','2','3','4','5','6','8','9','A','b','d','E','F']:
            j = j + 1
        else:
            break
    if j != len(ShowH):
        print("请不要输入”0123456789AbdEF“以外的字符")
        InputH()
    return ShowH

def Initial(width, hight, x, y):
    turtle.setup(width, hight, x, y)
    turtle.penup()
    turtle.fd(-350)

def SegShowDateMain():
    PrintIntro()
    Initial(800, 350, 200, 200)
    turtle.speed(5000)
    DrawDate(InputDate())
    turtle.hideturtle()
    turtle.done()
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition

def SegShowHMain():
    PrintIntro()
    Initial(800, 350, 200, 200)
    turtle.speed(5000)
    DrawH(InputH())
    turtle.hideturtle()
    turtle.done()
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
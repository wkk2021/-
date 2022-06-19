from random import random
from re import A

def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值、天气情况权重以及两位选手失误概率(以0到1之间的小数表示)")

def InputAbil(name, asp):
    try:
        a = eval(input("请输入选手{}的{}(0-1): " .format(name, asp)))
        if a < 0 or a >= 1:
            print("请输入(0-1)的{}!" .format(asp))
            a = InputAbil(name)
    except NameError:
        print("请输入(0-1)的{}!" .format(asp))
        a = InputAbil(name)
    return a

def InputScreenings():
    try:
        a = eval(input("请输入模拟比赛场次： " ))
        if a <=0:
            print("输入的比赛场次应大于等于1!")
            a = InputScreenings()
    except NameError:
        print("输入的比赛场次应大于等于1!")
        a = InputScreenings()
    return a

def InputWeather():
    try:
        a = eval(input("请输入天气情况权重值(0-1): "))
        if a < 0 or a >= 1:
            print("输入(0-1)的天气权重值!")
            a = InputWeather()
    except NameError:
        print("输入(0-1)的天气权重值!")
        a = InputWeather()
    return a

def getInputs():
    Name = ['A', 'B']
    Charact = ["能力值", "失误概率"]
    Weather = ["下雨", "下雪", "大雾"]
    k = 0
    l = [1, 2, 3, 4]
    for i in Name:
        for j in Charact:
            l[k] = InputAbil(i, j)
            k += 1
    c = InputWeather()
    a = l[0]
    b = l[2]
    d = l[1]
    e = l[3]
    n = InputScreenings()
    return a, b, c, d, e, n

def simNGames(n, probA, probB, missA, missB, weather):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, missA, missB, weather)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def gameOver(a,b):
    return a==15 or b==15

def simOneGame(probA, probB, missA, missB, weather):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            a = random()
            b = random()
            c = random()
            if a < probA and b >= missA and c >= weather:
                scoreA += 1
            else:
                serving = "B"
        else:
            a = random()
            b = random()
            c = random()
            if a < probB and b >= missB and c >= weather:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))

def MatchAnalysisMain():
    printIntro()
    probA, probB, weather, missA, missB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB, missA, missB, weather)
    printSummary(winsA, winsB)

if __name__ == '__main__':
    MatchAnalysisMain()
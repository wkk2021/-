def NameInput():
    a = input("请输入文件名称：")
    if ".py" not in a:
        a = a + ".py"
    try:
        b = open("E:\python_homwork\{}" .format(a), encoding = 'utf-8')
        b.close()
    except FileNotFoundError:
        print("请输入正确的文件名称！")
        a = NameInput()
    return a

def GetContent():
    Name = NameInput()
    Txt = open("E:\python_homwork\{}" .format(Name), encoding = 'utf-8').read()
    for Ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        Txt = Txt.replace(Ch, " ")
    return Txt

def CalNum(Txt):
    List = Txt.split()
    Counter = {}
    for Word in List:
        Counter[Word] = Counter.get(Word, 0) + 1
    items = list(Counter.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(10):
        Word, Count = items[i]
        print("{0:<10}{1:>5}" .format(Word, Count))

def CalWordMain():
    Txt = GetContent()
    CalNum(Txt)

if __name__ == '__main__':
    CalWordMain()
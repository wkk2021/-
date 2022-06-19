import HashFunction, Python, Wu, SegShow, CalWord, MatchAnalysis, Reptile
def ContentShowMain():
    print("\n请输入指定数字进行以下演示:\n哈希函数演示请输入1\n蟒蛇演示请按2\n写汉字演示请输入3\n数码管显示演示请输入4\n统计词频演示请输入5\n模拟比赛演示请输入6\n爬虫演示请输入7")

def ContentShowSeg():
    print("请输入指定字符进行以下演示：\n日期显示请输入1\n十六进制数显示请输入2\n返回主菜单#")

def ContentInFirst():
    ContentIn = input("请输入数字：")
    if ContentIn not in ['1','2','3','4', '5','6', '7']:
        print("输入错误，请输入指定数字：")
        ContentIn = ContentInFirst()
    return ContentIn

def ContentInSeg():
    ContentShowSeg()
    ContentIn = input("请输入菜单字符：")
    if ContentIn not in ['1','2','#']:
        print("输入错误，请输入指定字符：")
        ContentIn = ContentInSeg()
    return ContentIn

def ShowSeg():
    ContentSeg = ContentInSeg()
    if ContentSeg == '1':
        SegShow.SegShowDateMain()
        BackorEnd()
    elif ContentSeg == '2':
        SegShow.SegShowHMain()
        BackorEnd()
    else:
        ContentShowMain()
        ContentShowNext()

def BackorEndIn():
    Order = input("请输入指定命令：")
    if Order not in ['#', 'e']:
        Order = BackorEndIn()
    return Order

def BackorEnd():
    print("\n演示结束，返回主菜单请输入'#'\n结束演示请输入'e'")
    Order = BackorEndIn()
    if Order == '#':
        ContentShowMain()
        ContentShowNext()

def ContentShowNext():
    Content = ContentInFirst()
    ContentMain = ["哈希函数","蟒蛇","写汉字","数码管显示", "词频统计", "模拟比赛", "爬虫"]
    print("\n下面进行{}演示：".format(ContentMain[eval(Content)-1]))
    if Content == '4':
        ShowSeg()
    elif Content == '1':
        HashFunction.HashMain()
        BackorEnd()
    elif Content == '2':
        Python.PythonMain()
        BackorEnd()
    elif Content == '3':
        Wu.Wumain()
        BackorEnd()
    elif Content == '5':
        CalWord.CalWordMain()
        BackorEnd()
    elif Content == '6':
        MatchAnalysis.MatchAnalysisMain()
        BackorEnd()
    elif Content == '7':
        Reptile.ReptileMain()
        BackorEnd()

def main():
    ContentShowMain()
    ContentShowNext()

if __name__ == '__main__':
    main()
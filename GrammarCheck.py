def PrintIntro():
    print("这个程序对所输入python文件进行基本语法检查")
    print("这个程序需要输入进行语法检查的文件名称")

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

def OpenFile():
    Name = NameInput()
    File = open("E:\python_homwork\{}" .format(Name), encoding = 'utf-8')
    return File

def DeletLeftSpace(File):
    Lines = File.readlines()
    for i in range(len(Lines)):
        Lines[i] = Lines[i].strip()
    return Lines

def CheckIf(Lines):
    num = 0
    error = {}
    for line in Lines:
        num = num +1
        if (line[:3] == "if ") and (line[-1] == ':') and (line[2:-1] != " "*(len(line)-3)):
            continue
        elif (line[:3] == "if ") and (line[-1] != ':'):
            error[num] = "if条件语句缺少':'!"
        elif (line[:3] == "if ") and (line[-1] == ':') and (line[2:-1] == " "*(len(line)-3)):
            error[num] = "if条件语句缺少判断条件!"
        elif (line[:2] == "if") and (line[-1] == ':') and (line[2] != ' '):
            error[num] = "保留字if应该使用空格与其他部分隔开!"
        else:
            continue
    return error

def CheckFor(Lines):
    num = 0
    error = {}
    for line in Lines:
        num = num + 1
        Lco = line.find(" in ")
        if (line[:4] == "for ") and (" in " in line) and (line[3:(Lco+1)] != " "*(Lco-2)) and (line[(Lco+3):-1] != " "*(len(line)-Lco-4)) and (line[-1] == ':'):
            continue
        elif (line[:4] == "for ") and (" in " in line) and (line[3:(Lco+1)] != " "*(Lco-2)) and (line[(Lco+3):-1] != " "*(len(line)-Lco-4)) and (line[-1] != ':'):
            error[num] = "for循环语句缺少':'!"
        elif (line[:4] == "for ") and (" in " in line) and ((line[3:(Lco+1)] == " "*(Lco-2)) or (line[(Lco+3):-1] != " "*(len(line)-Lco-4))) and (line[-1] == ':'):
            error[num] = "for循环语句的循环条件不完整!"
        elif (line[:3] == "for") and (" in " in line) and (line[-1] == ':') and (line[3] != " "):
            error[num] ="保留字for应该使用空格与其他部分隔开!"
        else:
            continue
    return error

def CheckTry(Lines):
    num = 0
    error = {}
    for line in Lines:
        num = num + 1
        n = num 
        if (line[:3] == "try") and (line[-1] == ':'):
            for i in Lines[num:]:
                n = n + 1
                l = len(i)
                if (i[:7] == "except ") and (i[-1] == ':') and (i[6:l-1] != " "*(l-7)):
                    if (num == n-1) or (''.join(Lines[num:n-1]) == ""):
                        error[num + 1] = "没有程序被监测异常并处理！"
                    else:
                        break
                elif (i[:7] == "except ") and (i[-1] == ':') and (i[6:l-1] == " "*(l-7)):
                    error[n] = "请指出被检测并处理的异常"
                elif (i[:7] == "except ") and (i[-1] != ':') and (i[6:l-1] != " "*(l-7)):
                    error[n] = "except语句缺少':'!"
                else:
                    continue
        elif (line[:3] == "try") and (line[-1] != ':'):
            error[num] = "try语句缺少':'!"
        else:
            continue
    return error

def Sort(List):
    Len = len(List)
    for i in range(0, Len-1):
        if List[i] > List[i + 1]:
           List[i], List[i + 1] = List[i + 1], List[i]
    return List

def PrintError(Lines):
    ErrorIf = CheckIf(Lines)
    ErrorFor = CheckFor(Lines)
    ErrorTry = CheckTry(Lines)
    Error = {}
    for NameIf in ErrorIf:
        Error[NameIf] = ErrorIf[NameIf]
    for NameFor in ErrorFor:
        Error[NameFor] = ErrorFor[NameFor]
    for NameTry in ErrorTry:
        Error[NameTry] = ErrorTry[NameTry]
    if Error == {}:
        print("语法正确!")
    else:
        List = list(Error.keys())
        List = Sort(List)
        num = 0
        for i in List:
            num = num +1
            print("Error{}: 第{}行  {}" .format(num, i, Error[i]))

def GrammarCheckMain():
    PrintIntro()
    File = OpenFile()
    Lines = DeletLeftSpace(File)
    PrintError(Lines)
    File.close
    
if __name__ == '__main__':
    GrammarCheckMain()
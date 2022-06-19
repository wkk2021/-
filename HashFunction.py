def PrintIntro():
    print("这个程序对所输入的数字进行哈希编码")
    print("这个程序需要输入所需编码的数字")

def HashInNums():
    InNumber = input("请输入待编码数字：").split()
    try:
        eval(''.join(InNumber))
    except SyntaxError:
        print("请注意不要输入其他字符！")
        InNumber = HashInNums()
    except NameError:
        print("请注意不要输入其他字符！")
        InNumber = HashInNums()
    except ValueError:
        print("请注意不要输入其他字符！")
        InNumber = HashInNums()
    InNumber = list(map(int, InNumber))
    return InNumber

def HashCoding(InNumber):
    AddrDict = {}
    n = len(InNumber)
    for i in range(n):
        AddrDict[i] = ''
    for j in range(n):
        Addr = InNumber[j] % n
        if AddrDict[Addr] == '':
                AddrDict[Addr] = InNumber[j]
        else:
            for k in range(1,n):
                FindAddr = (Addr + k) % n
                if AddrDict[FindAddr] == '':
                    AddrDict[FindAddr] = InNumber[j]
                    break
    return AddrDict

def HashMain():
    InNumber = HashInNums()
    AddrDict = HashCoding(InNumber)
    print(AddrDict)

if __name__ == '__main__':
    HashMain()
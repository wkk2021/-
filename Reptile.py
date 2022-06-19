import requests
from bs4 import BeautifulSoup
import re
import json
def PrintIntro():
    print("这个程序爬取所有有关关键词的网页地址")
    print("这个程序需要输入进行爬取的关键词")

def getKeywordResult(keyword):
    if "http" not in keyword:
        url = 'http://www.baidu.com/s?wd='+keyword
    else:
        url = keyword
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def parserLinks(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for div in soup.find_all("div", {"data-tools": re.compile("url")}):
        data = div.attrs['data-tools']
        data = data.replace("'", '"')
        d = json.loads(data)
        links.append(d['url'])
    return links

def Recursion(links, file):
    for link in links: 
        a = link + '\n'
        file.write(a)
        Content =  getKeywordResult(link)
        Links = parserLinks(Content)
        if len(Links) == 0:
            continue
        else:
            Recursion(Links, file)
def Input():
    name = input("请输入想要搜索的关键词：")
    return name

def ReptileMain():
    PrintIntro()
    name = Input()
    html = getKeywordResult(name)
    ls = parserLinks(html)
    file = open(r"E:\python_homwork\{}.txt" .format(name), "w", encoding='utf-8')
    Recursion(ls, file)
    file.close()

if __name__ == '__main__':
    ReptileMain()
import requests
from bs4 import BeautifulSoup


urlakxw = "http://www.ahstu.edu.cn/index/akxw.htm"
urltest = "https://www.baidu.com/"
content = requests.get(urlakxw)
content.encoding="UTF-8"

soup = BeautifulSoup(content.text, 'lxml')
# source = open("reptiletest.html", "w")
# source.write(content.text)
# source.close()
# NewsList = open('newslist.txt', 'w', encoding='utf-8')
# li = soup.find_all('span', attrs={'class':'conListWord'})
# newli = li.span.extract()
# print(newli)
# for line in li:
#     print(line, file=NewsList)
# NewsList.close()
# lin作为一个标签，属于一个tag
for link in soup.find_all('a', attrs={'class':'rigthConBox-conList'}):
    # print(type(link)) # <class 'bs4.element.Tag'>
    spanlist = link.find_all('span', attrs={'class':['conListWord', 'conListTime'], })
    # find_all 字典的key对应的value是一个list就可以多个查询
    # 对tag可以使用find方法，查找tag内部的其他标签
    # type(spanlist) <class 'bs4.element.ResultSet'>
    # spanlist内包含的每一个标签还是一个tag
    # type(spanlist[0]) <class 'bs4.element.Tag'>
    for span in spanlist:
        print(span.string, end=' ')
    print()

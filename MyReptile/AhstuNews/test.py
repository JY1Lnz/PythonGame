import requests
import queue
import re
from bs4 import BeautifulSoup

# urlakxw = "http://www.ahstu.edu.cn/index/akxw.htm"
# urltzgg = ""
# urltest = "https://www.baidu.com/"
# content = requests.get(urlakxw)
# content.encoding="UTF-8"
#
# soup = BeautifulSoup(content.text, 'lxml')
# # source = open("reptiletest.html", "w")
# # source.write(content.text)
# # source.close()
# # NewsList = open('newslist.txt', 'w', encoding='utf-8')
# # li = soup.find_all('span', attrs={'class':'conListWord'})
# # newli = li.span.extract()
# # print(newli)
# # for line in li:
# #     print(line, file=NewsList)
# # NewsList.close()
# # lin作为一个标签，属于一个tag
# newsdict = {}
# for link in soup.find_all('a', attrs={'class':'rigthConBox-conList'}):
#     # type(link) <class 'bs4.element.Tag'>
#     spanlist = link.find_all('span', attrs={'class':['conListWord', 'conListTime'], })
#     linkurl = link.get('href')  # 获取每条信息的页面url
#     if (re.match('\.\.', linkurl)):  # 处理内部url,增加首部域名
#         linkurl = 'http://www.ahstu.edu.cn'+linkurl[2:]
#     linkname = spanlist[0].string
#     linkdate = spanlist[1].string
#     newsdict[linkname] = [linkurl, linkdate]
#     # find_all 字典的key对应的value是一个list就可以多个查询
#     # 对tag可以使用find方法，查找tag内部的其他标签
#     # type(spanlist) <class 'bs4.element.ResultSet'>
#     # spanlist内包含的每一个标签还是一个tag
#     # type(spanlist[0]) <class 'bs4.element.Tag'>
#     # print(urllist)
#     # for span in spanlist:
#     #     print(span.string, end=' ')
#     # print()
#     # 读取新闻条目，具体日期
#
# for key in newsdict:
#     print(newsdict[key])

# url = 'http://www.ahstu.edu.cn/info/1014/20693.htm'
# content = requests.get(url)
# content.encoding = 'utf-8'
# soup = BeautifulSoup(content.text, 'lxml')
# linkstart = soup.find('p', attrs={'class': 'vsbcontent_start'})
# linkend = soup.find('p', attrs={'class': 'vsbcontent_end'})
# linknext = linkstart.find_next('p')
# newscontent = ""
# while linkstart != linkend:
#     if linkstart.string:
#         newscontent += linkstart.string + '\n'
#     linkstart = linkstart.find_next('p')
# newscontent += linkstart.string
# # print(newscontent)
# # print(linkstart.string)
# # print(linkend.string)

url = 'http://www.ahstu.edu.cn/index/tzgg.htm'
# url[:-4] -> http://www.ahstu.edu.cn/index/tzgg
# http://www.ahstu.edu.cn/index/tzgg/86.htm
content = requests.get(url)
content.encoding = 'utf-8'
soup = BeautifulSoup(content.text, 'lxml')

link = soup.find('td', attrs={'id': 'fanye127268'})
page = str(link.string)
_, pagesum = page.split('/')
print(pagesum)
pagesum = int(pagesum)-1
for i in range(pagesum):
    nexturl = url[:-4]+'/'+str(pagesum-i)+'.htm'
    print(nexturl)

#!/usr/bin/python
import re
from MyReptile.AhstuNews.MyGetContent import ReptileContent

getcontent = ReptileContent.GetContent()
newsdict = getcontent.getstart()
print("获取结束，开始分析")
for key in newsdict:
    if re.search('信息', key):
        print(key)
        filename = 'newscontent/'+key+'.txt'
        news = open(filename, 'w', encoding='utf-8')
        newscontent = getcontent.gtnewscontent(newsdict[key][0])
        print(newscontent, file=news)
        news.close()

#!/usr/bin/python
import re
from MyReptile.AhstuNews.MyGetContent import ReptileContent

getcontent = ReptileContent.GetContent()
newsdict = getcontent.getstart()

for key in newsdict:
    if re.search('信息', key):
        filename = 'newscontent/'+key+'.txt'
        news = open(filename, 'w', encoding='GBK')
        newscontent = getcontent.gtnewscontent(newsdict[key][0])
        print(newscontent, file=news)
        news.close()

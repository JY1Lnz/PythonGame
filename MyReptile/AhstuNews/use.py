#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')  # 使在终端运行时可以正确定位库
from MyReptile.AhstuNews.MyGetContent import ReptileContent

getcontent = ReptileContent.GetContent()
newsdict = getcontent.getstart()
print("获取结束，开始分析")
number = 0
for key in newsdict:
    if re.search('信息', key):
        number += 1
        print(key)
        filename = 'MyReptile/AhstuNews/newscontent/'+key+'.txt'
        news = open(filename, 'w', encoding='utf-8')
        newscontent = getcontent.gtnewscontent(newsdict[key][0])
        print(newscontent, file=news)
        news.close()
print("共"+str(number)+"条信息")

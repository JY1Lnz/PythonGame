#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
from MyReptile.AhstuNews.MyGetContent import ReptileContent


class Run(object):
    """
    爬虫主程序
    """
    def __init__(self):
        self.Reptile = ReptileContent.GetContent()
        self.newsdict = self.Reptile.getstart()

    def analysis(self):
        """正则表达式匹配信息"""
        print("获取信息结束，开始分析")
        number = 0
        for key in self.newsdict:
            if re.search('信息', key):
                number += 1
                print(key)
                filename = 'MyReptile/AhstuNews/newscontent/'+key+'.txt'
                news = open(filename, 'w', encoding='utf-8')
                newscontent = self.Reptile.getnewscontent(self.newsdict[key][0])
                print(newscontent, file=news)
                news.close()
        print("共"+str(number)+"条有关消息")

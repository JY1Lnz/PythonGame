import requests
import re
import time
import datetime
from bs4 import BeautifulSoup


class GetContent(object):
    """
        爬取官网新闻内容，日期， 链接
    """
    def __init__(self):
        """初始化链接"""
        self.head = 'http://www.ahstu.edu.cn/'
        self.urllist = [
            'http://www.ahstu.edu.cn/index/akxw.htm',
            'http://www.ahstu.edu.cn/index/tzgg.htm',
            'http://www.ahstu.edu.cn/index/xydt.htm',
            'http://www.ahstu.edu.cn/index/xsxx.htm',
            'http://www.ahstu.edu.cn/index/mtak.htm',
        ]
        self.date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.year, self.month, self.day = map(int, self.date.split('-'))
        self.thisday = datetime.datetime(self.year, self.month, self.day)
        # self.urlakxw = 'http://www.ahstu.edu.cn/index/akxw.htm'  # 安科新闻
        # self.urltzgg = 'http://www.ahstu.edu.cn/index/tzgg.htm'  # 通知公告
        # self.urlxydt = 'http://www.ahstu.edu.cn/index/xydt.htm'  # 校园动态
        # self.urlxsxx = 'http://www.ahstu.edu.cn/index/xsxx.htm'  # 学术信息
        # self.urlmtak = 'http://www.ahstu.edu.cn/index/mtak.htm'  # 媒体安科

    def getnewstitle(self, url):
        """获取新闻具体标题"""
        content = requests.get(url)
        content.encoding = 'utf-8'
        contentsoup = BeautifulSoup(content.text, 'lxml')
        newstitle = contentsoup.find('div', attrs={'class': 'list-textT'})
        if newstitle:
            return newstitle.string
        return None

    def gtnewscontent(self, url):
        """获取新闻具体内容"""
        content = requests.get(url)
        content.encoding = 'utf-8'
        contentsoup = BeautifulSoup(content.text, 'lxml')
        linkstart = contentsoup.find('p', attrs={'class': 'vsbcontent_start'})  # 内容开始段落
        linkend = contentsoup.find('p', attrs={'class': 'vsbcontent_end'})  # 内容结束段落
        newscontent = ""
        while linkstart != linkend:  # 循环找出所有内容段落，忽略图片
            if linkstart.string:
                for c in linkstart.string:
                    newscontent += c
                    if c == '。':
                        newscontent += '\n'
            linkstart = linkstart.find_next('p')
        try:
            for c in linkstart.string:
                newscontent += c
                if c == '。':
                    newscontent += '\n'
        except:
            pass
        return newscontent

    def getnews(self, url):
        """获取当前页新闻缩略标题和对应链接以字典保存"""
        content = requests.get(url)  # 爬取内容
        content.encoding = 'utf-8'
        contentsoup = BeautifulSoup(content.text, 'lxml')  # beautifulsoup4分析
        newsdict = {}  # 保存新闻对应的url和日期
        for link in contentsoup.find_all('a', attrs={'class': 'rigthConBox-conList'}):
            spanlist = link.find_all('span', attrs={'class': ['conListWord', 'conListTime']})
            newsurl = link.get('href')
            while re.match('\.\.', newsurl):
                newsurl = newsurl[3:]
            newsurl = self.head+newsurl
            newsname = self.getnewstitle(newsurl)
            if not newsname:
                newsname = spanlist[0].string
            newsdate = str(spanlist[1].string)
            nowyear, nowmonth, nowday = map(int, newsdate.split('-'))
            thatday = datetime.datetime(nowyear, nowmonth, nowday)
            if (self.thisday-thatday).days > 7:
                return newsdict, False
            print("获得："+newsdate+"  "+newsname)
            newsdict[newsname] = [newsurl, newsdate]
        return newsdict, True

    def getpagesum(self, url):
        """获取新闻类别的总页数"""
        content = requests.get(url)
        content.encoding = 'utf-8'
        contentsoup = BeautifulSoup(content.text, 'lxml')
        pagecontent = contentsoup.find('td', attrs={'id': 'fanye127268'})
        pagecontent = str(pagecontent.string)
        _, pagesum = pagecontent.split('/')
        return int(pagesum)

    def getstart(self):
        """爬虫入口"""
        newsdict = {}
        for url in self.urllist:
            pagesum = self.getpagesum(url)-1  # 获取分类总页数，同时忽略首页
            thisnewsdict, _ = self.getnews(url)
            newsdict.update(thisnewsdict)  # 先获取首页信息
            for i in range(pagesum):
                nexturl = url[:-4]+'/'+str(pagesum-i)+'.htm'
                thisnewsdict, flag = self.getnews(nexturl)
                newsdict.update(thisnewsdict)
                if not flag:
                    break
        return newsdict

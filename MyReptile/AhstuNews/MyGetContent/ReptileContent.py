import requests
import re
from bs4 import BeautifulSoup


class GetContent(object):
    """
        爬取官网新闻内容，日期， 链接
    """
    def __init__(self):
        """初始化链接"""
        self.head = 'http://www.ahstu.edu.cn'
        self.urllist = [
            'http://www.ahstu.edu.cn/index/akxw.htm',
            'http://www.ahstu.edu.cn/index/tzgg.htm',
            'http://www.ahstu.edu.cn/index/xydt.htm',
            'http://www.ahstu.edu.cn/index/xsxx.htm',
            'http://www.ahstu.edu.cn/index/mtak.htm',
        ]
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
        for c in linkstart.string:
            newscontent += c
            if c == '。':
                newscontent += '\n'
        return newscontent

    def getnews(self, url):
        content = requests.get(url)  # 爬取内容
        content.encoding = 'utf-8'
        contentsoup = BeautifulSoup(content.text, 'lxml')  # beautifulsoup4分析
        newsdict = {}  # 保存新闻对应的url和日期
        for link in contentsoup.find_all('a', attrs={'class': 'rigthConBox-conList'}):
            spanlist = link.find_all('span', attrs={'class': ['conListWord', 'conListTime']})
            newsurl = link.get('href')
            if re.match('\.\.', newsurl):
                newsurl = self.head+newsurl[2:]
            newsname = self.getnewstitle(newsurl)
            if not newsname:
                newsname = spanlist[0].string
            newsdate = spanlist[1].string
            print("获得："+newsname)
            newsdict[newsname] = [newsurl, newsdate]
        return newsdict

    def getstart(self):
        newsdict = {}
        for url in self.urllist:
            newsdict.update(self.getnews(url))
        return newsdict

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
        self.urlakxw = 'http://www.ahstu.edu.cn/index/akxw.htm'  # 安科新闻
        self.urltzgg = 'http://www.ahstu.edu.cn/index/tzgg.htm'  # 通知公告
        self.urlxydt = 'http://www.ahstu.edu.cn/index/xydt.htm'  # 校园动态
        self.urlxsxx = 'http://www.ahstu.edu.cn/index/xsxx.htm'  # 学术信息
        self.urlmtak = 'http://www.ahstu.edu.cn/index/mtak.htm'  # 媒体安科

    def GetNewsContent(self, url):
        """或取新闻具体内容"""
        content = requests.get(url)
        content.encoding = 'utf-8'
        contentsoup = BeautifulSoup(content.text, 'lxml')
        newstitle = contentsoup.find('div', attrs={'class': 'list-textT'})
        if newstitle:
            return newstitle.string
        return None

    def GetNews(self, url):
        content = requests.get(url)  # 爬取内容
        content.encoding = 'utf-8'
        contentsoup = BeautifulSoup(content.text, 'lxml')  # beautifulsoup4分析
        newsdict = {}  # 保存新闻对应的url和日期
        for link in contentsoup.find_all('a', attrs={'class': 'rigthConBox-conList'}):
            spanlist = link.find_all('span', attrs={'class': ['conListWord', 'conListTime']})
            newsurl = link.get('href')
            if re.match('\.\.', newsurl):
                newsurl = self.head+newsurl[2:]
            newsname = self.GetNewsContent(newsurl)
            if not newsname:
                newsname = spanlist[0].string
            newsdate = spanlist[1].string
            newsdict[newsname] = [newsurl, newsdate]
        return newsdict

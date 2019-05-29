import requests
import re
from bs4 import BeautifulSoup

class GetContent(object):
    """
        爬取官网新闻内容，日期， 链接
    """
    def ___init__(self):
        self.urlakxw = 'http://www.ahstu.edu.cn/index/akxw.htm'  # 安科新闻
        self.urltzgg = 'http://www.ahstu.edu.cn/index/tzgg.htm'  # 通知公告
        self.urlxydt = 'http://www.ahstu.edu.cn/index/xydt.htm'  # 校园动态
        self.urlxsxx = 'http://www.ahstu.edu.cn/index/xsxx.htm'  # 学术信息
        self.urlmtak = 'http://www.ahstu.edu.cn/index/mtak.htm'  # 媒体安科

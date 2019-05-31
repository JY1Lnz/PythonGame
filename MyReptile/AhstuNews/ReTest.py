import re
import requests
from MyReptile.AhstuNews.MyGetContent import ReptileContent

url = 'http://www.ahstu.edu.cn/info/1016/20726.htm'
getcontent = ReptileContent.GetContent()
newscontent = getcontent.gtnewscontent('http://www.ahstu.edu.cn/../info/1016/20726.htm')
print(newscontent)

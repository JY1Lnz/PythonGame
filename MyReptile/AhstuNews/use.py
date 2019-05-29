import re
from MyReptile.AhstuNews.MyGetContent import ReptileContent

getcontent = ReptileContent.GetContent()
akxwdict = getcontent.GetNews(getcontent.urlakxw)
tzggdict = getcontent.GetNews(getcontent.urltzgg)
xydtdict = getcontent.GetNews(getcontent.urlxydt)
xsxxdict = getcontent.GetNews(getcontent.urlxsxx)

newsdict = {}
newsdict.update(akxwdict)
newsdict.update(tzggdict)
newsdict.update(xydtdict)
newsdict.update(xsxxdict)

for key in newsdict:
    if (re.search('信息', key)):
        print(key)

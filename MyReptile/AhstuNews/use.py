from MyReptile.AhstuNews.MyGetContent import ReptileContent

getcontent = ReptileContent.GetContent()
newsakxwdict = getcontent.GetContent(getcontent.urlakxw)

for key in newsakxwdict:
    print(key, ':', newsakxwdict[key])

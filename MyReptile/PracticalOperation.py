import requests

url = 'https://wj.qq.com/stat/overview.html?sid=3709512'

r = requests.get(url)
r.encoding='utf-8'
print(r.text)
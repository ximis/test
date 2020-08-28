import requests
from bs4 import BeautifulSoup

'''
使用笔趣阁来抓取小说，尝试
'''

if __name__ == '__main__':
    target = 'https://www.biqukan.com/38_38836/572071845.html'
    # target = 'https://www.biqukan.com/1_1094/5433843.html'
    req = requests.get(url=target)
    print(req.text)
    html = req.text
    bf = BeautifulSoup(html, "lxml")
    texts = bf.find_all('div', attrs={"class": 'showtxt'})
    print(texts)
    print(texts[0].text.replace("\u3000" * 2, '\n\n'))
    # 现在要有其他的方式来换行了。text直接获取就是文字。不好弄。

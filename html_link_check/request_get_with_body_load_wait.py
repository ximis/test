import requests
from bs4 import BeautifulSoup


def store(data, filename):
    with open(filename, 'w') as f:
        f.write(str(data))


url = "https://www.kucoin.com/"
res = requests.get(url)

soup = BeautifulSoup(res.content, 'lxml') #lxml为解析器
data_ls = soup.find_all('a')
for data in data_ls:
    pass


store(res.content, "data.log")

res = requests.get(url, timeout=15)
store(res.content, "data_timeout.log")

import time
with requests.get(url, stream=True) as r:
    time.sleep(15)
    print(r.headers)
    store(r.content, "data_stream.log")
    pass

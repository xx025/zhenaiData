import gzip
from urllib.request import Request, urlopen

from requests import RequestException

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '请填入自己的Cookie',
    'Host': 'www.zhenai.com',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 '
}


# 此函数块来自https://cuiqingcai.com/5052.html略作改动
def get_one_page(url_, headers_):
    req = Request(url=url_, headers=headers_, method='POST')
    try:
        response = urlopen(req)
        if response.getcode() == 200:
            return gzip.decompress(response.read()).decode('utf8')
        return None
    except RequestException:
        return None

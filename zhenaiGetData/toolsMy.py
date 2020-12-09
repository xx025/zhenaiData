import gzip
from urllib.request import Request, urlopen
from requests import RequestException
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'sid=f3555228-8d4e-42cf-b7b2-707d5ea40be4; __channelId=901045%2C0; ec=Ep3QIiQe-1607348275299-97f0f6b9bdae9-960316237; _efmdata=9B3BUAJ8GgaEUg29RWGNB%2BIhzyryMXs5UPHvvlXHCi4OaoTQ%2BMkMKbNGrW4gqf5e3ymKMbpjZLePdhxwpehlkZA%2FPgEZToCc%2B5DftTfpsKg%3D; _exid=CMvKnIQwjRJYrnH692YjOrCUOrL53pNdl55%2FPzC%2BOgRWnwFnob3Lcxv5nWvLSZr3DQ2EnubTI8bVj8mHiM8xNA%3D%3D',
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

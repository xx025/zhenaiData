'''
获取城市页面并将城市和对应的链接写入数据库
'''
from bs4 import BeautifulSoup
from connectMysql import MySQLJDBC
from zhenaiGetData import toolsMy
url = 'http://www.zhenai.com/zhenghun'
msql = MySQLJDBC.msql
get_one_page = toolsMy.get_one_page
headers = toolsMy.headers
if __name__ == '__main__':
    # 城市列表页面
    html = get_one_page(url, headers)  # 获取页面
    soup = BeautifulSoup(html, "lxml")  # 格式化
    msql.getCon()  # 连接数据库
    counts = 0  # 记录写入条数
    for i in soup.findAll(name='dl', attrs={"class": 'city-list clearfix'})[0].findAll('a'):
        sql = 'insert INTO citylink(loc,link)VALUES(\'{}\', \'{}\')'.format(i.get_text(), i.get('href'))
        if msql.insert(sql) == 1:
            counts = counts + 1
            # print(sql)
    print("写入条数:" + str(counts))
    msql.close()  # 关闭连接

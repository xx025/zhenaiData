import json
import re
from time import sleep, time

from bs4 import BeautifulSoup

from connectMysql import MySQLJDBC
from zhenaiGetData import toolsMy

msql = MySQLJDBC.msql
headers = toolsMy.headers

get_one_page = toolsMy.get_one_page


def insertDatabase(dict_):
    counts = 0
    for i in dict_:
        sql = 'insert INTO memberdata(age,avatarURL,car,children,' \
              'constellation,education,height,house,introduceContent,' \
              'isRecommend,lastModTime,marriage,memberID,nickName,objectAge,' \
              'objectHight,objectMarriage,objectSalary,occupation,salary,sex,workCity)' + \
              'VALUES({0}, \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', {6}, \'{7}\', \'{8}\', ' \
              '\'{9}\', \'{10}\', \'{11}\', \'{12}\', \'{13}\', \'{14}\', \'{15}\', \'{16}\', \'{17}\',' \
              ' \'{18}\', \'{19}\', {20}, \'{21}\')'.format(
                  i['age'], i['avatarURL'], i['car'], i['children'], i['constellation'], i['education'], i['height'],
                  i['house'], i['introduceContent'], i['isRecommend'], i['lastModTime'], i['marriage'], i['memberID'],
                  i['nickName'], i['objectAge'], i['objectHight'], i['objectMarriage'], i['objectSalary'],
                  i['occupation'], i['salary'], i['sex'], i['workCity'])
        if msql.insert(sql) == 1:
            # print(sql)
            counts = counts + 1
    print("写入条数:" + str(counts))


def fun3(url):
    # 城市列表页面
    for i in range(1, 7):
        sleep(3)  # 休眠3秒
        url2 = url + str(i)
        print(url2)
        html = get_one_page(url2, headers)  # 获取页面
        soup = BeautifulSoup(html, "lxml")  # 格式化
        titles = soup.select("body  script")[1]  # CSS 选择器
        str3 = str(titles).strip('<script>').strip('</script>').replace('\n', '').replace('\r', '').replace(' ', '')
        str4 = re.findall("window.__INITIAL_STATE__=(.*?);\(function", str3)[0]
        c = json.loads(str4)  # json转字典
        insertDatabase(c["memberListData"]['memberList'])


if __name__ == '__main__':
    msql.getCon()
    sql = 'select * from citylink'
    list = msql.get_all(sql)
    for i in list:
        str2 = i[2] + '/'
        print(str2)
        print(time())
        fun3(str2)
        sleep(3)
    msql.close()

# @File    : DownImg.py.py

# coding: utf8
import _thread
import os
import re

from connectMysql import MySQLJDBC

os.makedirs('./image/', exist_ok=True)


def urllib_download(IMAGE_URL, ID, imgtype):
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './image/' + ID + imgtype)
    return True


def request_download(IMAGE_URL, ID, imgtype):
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/' + ID + imgtype, 'wb') as f:
        f.write(r.content)
        return True


def chunk_download(IMAGE_URL, ID, imgtype):
    import requests
    r = requests.get(IMAGE_URL, stream=True)
    with open('./image/' + ID + imgtype, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
            return True


def imgDown(url, filenem, imgtype,age):
    if os.path.exists("./image/"+filenem+imgtype):
        return True#文件已存在
    else:
        print(age+"文件不存在，开始下载:"+filenem+imgtype)
        if urllib_download(url, filenem, imgtype):
            return True
        elif request_download(url, filenem, imgtype):
            return True
        elif chunk_download(url, filenem, imgtype):
            return True
        else:
            return False


msql = MySQLJDBC.msql

msql.getCon()
sql = 'select avatarURL, memberID, age from memberdata where sex = 1   and age < 30 group by memberID order by age '
list = msql.get_all(sql)


def xiancheng(list):
    for i in list[::1]:
        imgTYPE = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', i[0])[0]
        if imgDown(url=i[0], filenem=i[1], imgtype=imgTYPE,age=str(i[2])):
            pass
        else:
            print("失败", i)

xiancheng(list)






msql.close()

# encoding = utf8
'''
工具类来自:https://blog.csdn.net/welun521/article/details/82960730
略作改动
'''
import pymysql
class MYSQL():
    # 初始化方法
    def __init__(self, host, port, user, passwd, dbName, charsets):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
        self.charsets = charsets
# 连接数据库
    def getCon(self):
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.dbName,
            charset=self.charsets
        )
        self.cursor = self.db.cursor()
# 关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()
# 查询列表数据
    def get_all(self, sql):
        res = None
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except:
            print("查询失败！")
        return res
# 插入数据
    def insert(self, sql):
        count = 0
        try:
            # self.getCon()
            count = self.cursor.execute(sql)
            self.db.commit()
            # self.close()
        except:
            print("操作失败！")
            self.db.rollback()
        return count
msql = MYSQL(host="127.0.0.1", port=3306, user="root", passwd="root", dbName="zhenai0x2", charsets="utf8")

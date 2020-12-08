from connectMysql.MySQLJDBC import msql

msql.getCon()
sql = 'select age,introduceContent from memberdata where sex=1 and age<30 '
list = msql.get_all(sql)

strrr=""
for i in list:
    strrr+=i[1]

msql.close()
print(strrr)
import jieba.analyse

from connectMysql.MySQLJDBC import msql



msql.getCon()

sql = 'select age,introduceContent,sex from memberdata  '
list = msql.get_all(sql)

strrrage = {"0-20": ["", ""], "20-30": ["", ""], "30-40": ["", ""], "40-50": ["", ""], "50-60": ["", ""], "60+": ["", ""]}

for i in list:
    fl = int(i[2])
    # print(fl)
    # print(type(fl))
    if i[0] < 20:
        strrrage["0-20"][fl] += i[1]
    elif i[0] < 30:
        strrrage["20-30"][fl] += i[1]
    elif i[0] < 40:
        strrrage["30-40"][fl] += i[1]
    elif i[0] < 50:
        strrrage["40-50"][fl] += i[1]
    elif i[0] < 60:
        strrrage["50-60"][fl] += i[1]
    else:
        strrrage["60+"][fl] += i[1]

msql.close()

print("")
for k in range(2):
    print("女" if k == 1 else "男", "======================")
    for i, j in strrrage.items():
        print(i, jieba.analyse.extract_tags(j[k]))
    print("\n")





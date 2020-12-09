import matplotlib.pyplot as plt

from zhenaiAnalyzeData import getData

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False


def pintSexCount():
    countSex = getData.sexCount
    plt.figure(dpi=450)
    plt.title('男女性别占比')
    plt.pie(x=[i[1] for i in countSex.items()], autopct='%.3f%%', labels=['男', '女'], startangle=90)
    plt.show()
    plt.savefig('性别比例.png')
    return


def pintAge():
    # 记录年龄人数
    countAge = getData.ageCount
    plt.figure(dpi=450)
    x1 = [i[1] for i in countAge['aLL'].items()]
    y1 = [i[0] for i in countAge['aLL'].items()]
    plt.subplot(2, 1, 1)
    l0 = plt.plot(y1, x1)
    plt.title('年龄分布')
    plt.xlabel('年龄')
    plt.ylabel('人数')
    x2 = [i[1] for i in countAge['Male'].items()]
    y2 = [i[0] for i in countAge['Male'].items()]
    x3 = [i[1] for i in countAge['Female'].items()]
    y3 = [i[0] for i in countAge['Female'].items()]
    plt.subplot(2, 1, 2)
    l1 = plt.plot(y2, x2, label='男')
    l2 = plt.plot(y3, x3, label='女')
    plt.xlabel('年龄')
    plt.ylabel('人数')
    plt.legend()
    plt.show()
    plt.savefig('年龄分布.png')
    return


def pintPie(dict, pointy=2, title='全部'):
    plt.figure(dpi=450)
    plt.subplot(122)  # 第一张图中的第一张子图
    plt.title('全部')
    plt.pie(x=[i[1] for i in dict['aLL'].items()], autopct='%.{}f%%'.format(pointy), labels=[i[0] for i in dict['aLL'].items()], startangle=90)
    plt.subplot(221)  # 第一张图中的第二张子图
    plt.title('男')
    plt.pie(x=[i[1] for i in dict['Male'].items()], autopct='%.{}f%%'.format(pointy), labels=[i[0] for i in dict['Male'].items()], startangle=90)
    plt.subplot(223)  # 第一张图中的第二张子图
    plt.title('女')
    plt.pie(x=[i[1] for i in dict['Female'].items()], autopct='%.{}f%%'.format(pointy), labels=[i[0] for i in dict['Female'].items()], startangle=90)
    plt.suptitle(title)
    plt.show()
    return


def pintEdu():
    # 受教育程度
    countEdu = getData.eduCount
    pintPie(dict=countEdu, title='受教育程度')
    return


def pintHouse(countHouse,title='住房情况'):
    # 记录购房人数
    pintPie(countHouse, 2, title)
    return


def pintMarriage(countMarriage,title='婚姻状况'):
    # 婚姻状况
    pintPie(countMarriage, 2, title)
    return


def pintchilddrenCount():
    # 是否有孩子
    countChildren = getData.childrenCount
    pintPie(countChildren, title='是否有孩子')
    return


def pintOccupation():
    countOccupation = getData.occunCount
    pintPie(countOccupation, title="职业")


# plt.table()
def main():
    # pintSexCount()
    pintHouse(getData.houseCount4060,title='40-60岁住房情况')
    # pintAge()
    # pintMarriage(getData.marriageCount)
    # pintMarriage(getData.marriageCount4060,title='40-60岁婚姻状况')
    # pintchilddrenCount()
    # pintEdu()
    # pintOccupation()


main()

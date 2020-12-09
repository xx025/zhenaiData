# @File    : getData.py.py
from connectMysql.MySQLJDBC import msql


# 向数据库查询并将数据放在字典中
def sql_dict(sql_, dict_):
    # 连接数据库
    msql.getCon()
    for i in msql.get_all(sql_):
        dict_[i[0]] = i[1]
    msql.close()


def getSexCount():
    # 记录男女人数
    sqlSex = 'select se.sex,count(*) from (select distinct * from memberdata) as se group by se.sex'
    countSex = {}
    sql_dict(sqlSex, countSex)
    return countSex


def getInfo(item, listsex={'aLL': ' ', 'Male': ' where sex=0 ', 'Female': ' where sex=0 '}):
    count = {'aLL': {}, 'Male': {}, 'Female': {}}
    for i, j in listsex.items():
        sql = 'select {},count(*) from (select distinct * from memberdata) as se {} group by {}'.format(item, j, item)
        sql_dict(sql, count[i])
    return count


# 统计相关数量
def main():
    listsex = {'aLL': ' where age between 40 and 60',
               'Male': ' where age between 40 and 60 AND sex=0 ',
               'Female': ' where age between 40 and 60 AND sex = 1'}
    houseCount = getInfo('house', listsex=listsex)
    print(houseCount)
    # childdrenCount = getInfo('children')
    # ageCount = getInfo('age')
    # eduCount = getInfo('education')
    # marriageCount = getInfo('marriage')
    # occunCount = getInfo('occupation')
    # listsex = {'aLL': ' where age between 40 and 60',
    #            'Male': ' where age between 40 and 60 AND sex=0 ',
    #            'Female': ' where age between 40 and 60 AND sex = 1'}
    # count4060 = getInfo('marriage', listsex=listsex)
    # return houseCount, childdrenCount, ageCount, eduCount, marriageCount, occunCount


main()

# 为节省资源，下面是def main()的统计结果
houseCount = {'aLL': {'住在单位宿舍': 2059, '和家人同住': 10242, '已购房': 21254, '打算婚后购房': 2429, '未填写': 8938, '租房': 5850},
              'Male': {'住在单位宿舍': 1033, '和家人同住': 3844, '已购房': 11981, '打算婚后购房': 1819, '未填写': 2838, '租房': 1725},
              'Female': {'住在单位宿舍': 1026, '和家人同住': 6398, '已购房': 9273, '打算婚后购房': 610, '未填写': 6100, '租房': 4125}}
houseCount4060 = {'aLL': {'住在单位宿舍': 683, '和家人同住': 3849, '已购房': 10143, '打算婚后购房': 735, '未填写': 3804, '租房': 2408},
                  'Male': {'住在单位宿舍': 317, '和家人同住': 1284, '已购房': 4608, '打算婚后购房': 512, '未填写': 979, '租房': 644},
                  'Female': {'住在单位宿舍': 366, '和家人同住': 2565, '已购房': 5535, '打算婚后购房': 223, '未填写': 2825, '租房': 1764}}

ageCount = {'aLL': {18: 59, 19: 52, 20: 110, 21: 188, 22: 311, 23: 427, 24: 729, 25: 1101, 26: 1227, 27: 1552, 28: 1680, 29: 1713, 30: 2197,
                    31: 2193, 32: 2179, 33: 2069, 34: 2005, 35: 1639, 36: 1500, 37: 1490, 38: 1663, 39: 1510, 40: 1417, 41: 1353, 42: 1397,
                    43: 1264, 44: 1377, 45: 1362, 46: 1417, 47: 1364, 48: 1397, 49: 1283, 50: 1475, 51: 1072, 52: 1051, 53: 694, 54: 712,
                    55: 735, 56: 640, 57: 669, 58: 472, 59: 207, 60: 264, 61: 178, 62: 244, 63: 210, 64: 189, 65: 148, 66: 140, 67: 95,
                    68: 78, 69: 59, 70: 49, 71: 50, 72: 31, 73: 15, 74: 15, 75: 11, 76: 10, 77: 8, 78: 5, 79: 5, 80: 2, 81: 1, 82: 3,
                    83: 4, 84: 4, 87: 1, 99: 1},
            'Male': {18: 30, 19: 31, 20: 47, 21: 92, 22: 166, 23: 208, 24: 358, 25: 521, 26: 643, 27: 831, 28: 908, 29: 932, 30: 1171,
                     31: 1152, 32: 1156, 33: 1055, 34: 1004, 35: 825, 36: 777, 37: 708, 38: 805, 39: 714, 40: 648, 41: 599, 42: 601,
                     43: 520, 44: 545, 45: 573, 46: 546, 47: 493, 48: 490, 49: 437, 50: 512, 51: 407, 52: 356, 53: 266, 54: 260,
                     55: 266, 56: 242, 57: 246, 58: 160, 59: 78, 60: 99, 61: 92, 62: 102, 63: 95, 64: 89, 65: 61, 66: 72, 67: 38,
                     68: 35, 69: 34, 70: 30, 71: 26, 72: 20, 73: 13, 74: 13, 75: 8, 76: 8, 77: 4, 78: 5, 79: 4, 80: 2, 81: 1,
                     82: 3, 83: 3, 84: 2, 87: 1, 99: 1},
            'Female': {18: 29, 19: 21, 20: 63, 21: 96, 22: 145, 23: 219, 24: 371, 25: 580, 26: 584, 27: 721, 28: 772, 29: 781, 30: 1026,
                       31: 1041, 32: 1023, 33: 1014, 34: 1001, 35: 814, 36: 723, 37: 782, 38: 858, 39: 796, 40: 769, 41: 754, 42: 796,
                       43: 744, 44: 832, 45: 789, 46: 871, 47: 871, 48: 907, 49: 846, 50: 963, 51: 665, 52: 695, 53: 428, 54: 452,
                       55: 469, 56: 398, 57: 423, 58: 312, 59: 129, 60: 165, 61: 86, 62: 142, 63: 115, 64: 100, 65: 87, 66: 68,
                       67: 57, 68: 43, 69: 25, 70: 19, 71: 24, 72: 11, 73: 2, 74: 2, 75: 3, 76: 2, 77: 4, 79: 1, 83: 1, 84: 2}}
eduCount = {'aLL': {'中专': 8104, '博士': 123, '大专': 12995, '大学本科': 11254, '硕士': 1224, '高中及以下': 17072},
            'Male': {'中专': 3525, '博士': 83, '大专': 6274, '大学本科': 5763, '硕士': 637, '高中及以下': 6958},
            'Female': {'中专': 4579, '博士': 40, '大专': 6721, '大学本科': 5491, '硕士': 587, '高中及以下': 10114}}
sexCount = {'male': 23240, 'female': 27532}
marriageCount = {'aLL': {'丧偶': 4313, '未婚': 16386, '未填写': 6, '离异': 30067},
                 'Male': {'丧偶': 1193, '未婚': 10516, '未填写': 5, '离异': 11526},
                 'Female': {'丧偶': 3120, '未婚': 5870, '未填写': 1, '离异': 18541}}

marriageCount4060 = {'aLL': {'丧偶': 3135, '未填写': 2, '未婚': 1374, '离异': 17111},
                     'Male': {'丧偶': 776, '未填写': 2, '未婚': 1059, '离异': 6507},
                     'Female': {'丧偶': 2359, '未婚': 315, '离异': 10604}}

childrenCount = {'aLL': {'有孩子且住在一起': 9466, '有孩子且偶尔会一起住': 5173, '有孩子但不在身边': 11530, '未填写': 7781, '没有小孩': 16822},
                 'Male': {'有孩子且住在一起': 2971, '有孩子且偶尔会一起住': 1721, '有孩子但不在身边': 5095, '未填写': 2800, '没有小孩': 10653},
                 'Female': {'有孩子且住在一起': 6495, '有孩子且偶尔会一起住': 3452, '有孩子但不在身边': 6435, '未填写': 4981, '没有小孩': 6169}}
occunCount = {'aLL': {'IT工程师': 171, 'IT技术总监': 101, 'IT技术经理': 48, '专业顾问': 75, '业务跟单': 20, '中学教师': 703, '临床研究': 9,
                      '主持人': 14, '主编': 20, '乘务员': 28, '交通运输': 432, '人事/行政': 536, '人事专员': 115, '人事主管': 139, '人事总监': 109,
                      '人事经理': 101, '仓库管理员': 60, '仓库经理': 8, '会计': 439, '传媒/艺术': 193, '作家': 10, '保安人员': 33, '保安经理': 5,
                      '保险': 73, '健身教练': 44, '公关专员': 2, '公关经理': 2, '公务员': 988, '其他职业': 5786, '兽医': 6, '军人/警察': 373,
                      '农林牧渔': 423, '出版发行': 13, '列车司机': 28, '副总经理': 65, '化工工程师': 9, '医生': 510, '医疗/护理': 362,
                      '医疗器械': 25, '医疗管理': 326, '医药代表': 20, '厨师': 190, '司机': 232, '合伙人': 280, '后勤': 102, '咨询/顾问': 80,
                      '咨询师': 34, '咨询经理': 11, '品牌专员': 1, '品牌经理': 10, '商务专员': 24, '商务经理': 130, '商场经理': 13, '商贸/采购': 155,
                      '在校学生': 129, '地勤人员': 65, '培训专员': 4, '培训师': 113, '培训经理': 13, '外贸专员': 45, '外贸经理': 34, '大堂经理': 15,
                      '媒介经理': 2, '安全管理': 160, '审计师': 10, '客户代表': 41, '客户服务': 179, '客户经理': 82, '客服专员': 84, '客服主管': 57,
                      '客服协调': 19, '客服技术支持': 49, '客服经理': 150, '家政服务': 85, '导游': 24, '导演': 8, '小学教师': 732, '工厂经理': 256,
                      '工程师': 1056, '市场拓展': 15, '市场策划': 11, '市场营销专员': 7, '市场营销经理': 17, '市场调研与分析': 5, '幼师': 252,
                      '广告/市场': 47, '广告客户专员': 1, '广告客户经理': 24, '广告策划': 23, '广告设计专员': 24, '广告设计经理': 15, '店员': 137,
                      '建筑/房地产': 933, '建筑师': 356, '影视后期制作': 18, '待业': 669, '律师': 43, '律师助理': 10, '心理医生': 8, '快递员': 37,
                      '总监': 113, '总经理': 294, '总裁助理': 16, '成本经理': 2, '房地产交易': 91, '房地产策划': 36, '投资': 176, '护士': 193, '报关员': 1,
                      '报单员': 1, '招聘专员': 14, '招聘经理': 9, '摄影师': 30, '撰稿人': 10, '操作工人': 547, '政府机构': 1008, '教务管理人员': 207,
                      '教授': 69, '教育/科研': 647, '文员': 205, '文案策划': 25, '景观设计': 45, '服务业': 892, '未填写': 7988, '模特': 8, '法务专员': 8,
                      '法务经理': 4, '法律': 59, '注册会计师': 9, '测试专员': 11, '渠道/分销专员': 57, '渠道/分销管理': 96, '演员': 19, '物业管理': 58,
                      '物料管理': 80, '物流/仓储': 136, '物流专员': 61, '物流主管': 42, '物流经理': 99, '生产/制造': 935, '生产领班': 222, '生物/制药': 87,
                      '生物工程': 39, '电子技术': 115, '画家': 12, '知识产权专员': 4, '科研人员': 62, '科研管理人员': 25, '秘书': 23, '税务专员': 7, '税务经理': 1,
                      '空乘人员': 7, '系统管理员': 30, '经理': 165, '经纪人': 2, '经销商': 435, '编辑': 46, '网站产品经理': 26, '网站编辑': 6, '网页设计': 25,
                      '美容师': 274, '职业技术教师': 64, '自由职业': 4403, '舞蹈': 32, '船员': 31, '船长': 7, '药剂师': 82, '药品生产': 22, '营运主管': 63,
                      '营运经理': 45, '规划师': 16, '计算机/互联网': 376, '记者': 9, '讲师/助教': 197, '设计师': 160, '证券': 56, '财会/审计': 192,
                      '财务主管': 103, '财务总监': 42, '财务经理': 55, '货运代理': 43, '车间主任': 86, '运营管理': 168, '通信/电子': 180, '通信技术': 212,
                      '酒店服务员': 38, '酒店管理': 117, '采购专员': 53, '采购经理': 41, '金融': 246, '金融/银行/保险': 164, '银行': 280, '销售': 1091,
                      '销售专员': 428, '销售主管': 408, '销售总监': 3735, '销售经理': 668, '集装箱业务': 16, '零售店店长': 97, '音乐家': 17, '项目主管': 198,
                      '飞行员': 10, '餐厅服务员': 64, '餐饮管理': 473, '高级管理': 320},
              'Male': {'IT工程师': 157, 'IT技术总监': 83, 'IT技术经理': 45, '专业顾问': 31, '业务跟单': 3, '中学教师': 229, '临床研究': 5, '主持人': 6, '主编': 4, '乘务员': 21,
                       '交通运输': 364, '人事/行政': 166, '人事专员': 20, '人事主管': 49, '人事总监': 41, '人事经理': 30, '仓库管理员': 33, '仓库经理': 7, '会计': 39, '传媒/艺术': 83,
                       '作家': 5, '保安人员': 28, '保安经理': 5, '保险': 19, '健身教练': 16, '公关专员': 1, '公关经理': 2, '公务员': 590, '其他职业': 2556, '兽医': 4,
                       '军人/警察': 331,
                       '农林牧渔': 320, '出版发行': 9, '列车司机': 26, '副总经理': 55, '化工工程师': 8, '医生': 211, '医疗/护理': 54, '医疗器械': 11, '医疗管理': 99, '医药代表': 11,
                       '厨师': 157, '司机': 219, '合伙人': 192, '后勤': 41, '咨询/顾问': 29, '咨询师': 12, '咨询经理': 5, '品牌经理': 5, '商务专员': 10, '商务经理': 89,
                       '商场经理': 4,
                       '商贸/采购': 107, '在校学生': 47, '地勤人员': 48, '培训专员': 4, '培训师': 40, '培训经理': 3, '外贸专员': 13, '外贸经理': 19, '大堂经理': 1, '媒介经理': 1,
                       '安全管理': 137, '审计师': 2, '客户代表': 14, '客户服务': 45,
                       '客户经理': 34, '客服专员': 9, '客服主管': 14, '客服协调': 3, '客服技术支持': 32, '客服经理': 43, '家政服务': 8, '导游': 9, '导演': 7, '小学教师': 139,
                       '工厂经理': 215,
                       '工程师': 936, '市场拓展': 7, '市场策划': 7, '市场营销专员': 1, '市场营销经理': 9, '市场调研与分析': 3, '幼师': 5, '广告/市场': 29, '广告客户经理': 16, '广告策划': 9,
                       '广告设计专员': 9, '广告设计经理': 5, '店员': 14, '建筑/房地产': 773, '建筑师': 326, '影视后期制作': 16, '待业': 131, '律师': 24, '律师助理': 2, '心理医生': 3,
                       '快递员': 33, '总监': 79, '总经理': 240, '总裁助理': 7, '成本经理': 2, '房地产交易': 46, '房地产策划': 22, '投资': 121, '护士': 5, '报关员': 1, '报单员': 1,
                       '招聘专员': 4, '招聘经理': 2, '摄影师': 22, '撰稿人': 4, '操作工人': 395, '政府机构': 573, '教务管理人员': 71, '教授': 35, '教育/科研': 199, '文员': 24,
                       '文案策划': 9,
                       '景观设计': 31, '服务业': 394, '未填写': 2732, '模特': 1, '法务专员': 4, '法务经理': 3, '法律': 31, '注册会计师': 5, '测试专员': 10, '渠道/分销专员': 24,
                       '渠道/分销管理': 46, '演员': 7, '物业管理': 40,
                       '物料管理': 47, '物流/仓储': 107, '物流专员': 48, '物流主管': 33, '物流经理': 74, '生产/制造': 759, '生产领班': 185, '生物/制药': 49, '生物工程': 28,
                       '电子技术': 104,
                       '画家': 8, '知识产权专员': 2, '科研人员': 40, '科研管理人员': 15, '秘书': 5, '税务专员': 1, '空乘人员': 3, '系统管理员': 26, '经理': 104, '经纪人': 1,
                       '经销商': 213,
                       '编辑': 14, '网站产品经理': 18, '网站编辑': 6, '网页设计': 5, '美容师': 9, '职业技术教师': 27, '自由职业': 1919, '舞蹈': 6, '船员': 31, '船长': 7, '药剂师': 18,
                       '药品生产': 15, '营运主管': 50, '营运经理': 40, '规划师': 15, '计算机/互联网': 269, '记者': 4, '讲师/助教': 81, '设计师': 84, '证券': 38, '财会/审计': 28,
                       '财务主管': 23, '财务总监': 9, '财务经理': 17, '货运代理': 39, '车间主任': 76, '运营管理': 94, '通信/电子': 127, '通信技术': 156, '酒店服务员': 4, '酒店管理': 41,
                       '采购专员': 25, '采购经理': 23, '金融': 127, '金融/银行/保险': 71, '银行': 120, '销售': 205, '销售专员': 85, '销售主管': 125, '销售总监': 1279,
                       '销售经理': 314,
                       '集装箱业务': 13, '零售店店长': 35, '音乐家': 11,
                       '项目主管': 165, '飞行员': 7, '餐厅服务员': 14, '餐饮管理': 213, '高级管理': 204},
              'Female': {'IT工程师': 14, 'IT技术总监': 18, 'IT技术经理': 3, '专业顾问': 44, '业务跟单': 17, '中学教师': 474, '临床研究': 4, '主持人': 8, '主编': 16, '乘务员': 7,
                         '交通运输': 68, '人事/行政': 370, '人事专员': 95, '人事主管': 90, '人事总监': 68, '人事经理': 71, '仓库管理员': 27, '仓库经理': 1, '会计': 400,
                         '传媒/艺术': 110,
                         '作家': 5, '保安人员': 5, '保险': 54, '健身教练': 28, '公关专员': 1, '公务员': 398, '其他职业': 3230, '兽医': 2, '军人/警察': 42, '农林牧渔': 103,
                         '出版发行': 4,
                         '列车司机': 2, '副总经理': 10, '化工工程师': 1, '医生': 299, '医疗/护理': 308, '医疗器械': 14, '医疗管理': 227, '医药代表': 9, '厨师': 33, '司机': 13,
                         '合伙人': 88, '后勤': 61, '咨询/顾问': 51, '咨询师': 22, '咨询经理': 6, '品牌专员': 1, '品牌经理': 5, '商务专员': 14, '商务经理': 41, '商场经理': 9,
                         '商贸/采购': 48,
                         '在校学生': 82, '地勤人员': 17, '培训师': 73, '培训经理': 10, '外贸专员': 32, '外贸经理': 15, '大堂经理': 14, '媒介经理': 1, '安全管理': 23, '审计师': 8,
                         '客户代表': 27, '客户服务': 134, '客户经理': 48, '客服专员': 75,
                         '客服主管': 43, '客服协调': 16, '客服技术支持': 17, '客服经理': 107, '家政服务': 77, '导游': 15, '导演': 1, '小学教师': 593, '工厂经理': 41, '工程师': 120,
                         '市场拓展': 8, '市场策划': 4, '市场营销专员': 6, '市场营销经理': 8, '市场调研与分析': 2, '幼师': 247, '广告/市场': 18, '广告客户专员': 1, '广告客户经理': 8,
                         '广告策划': 14,
                         '广告设计专员': 15, '广告设计经理': 10, '店员': 123, '建筑/房地产': 160, '建筑师': 30, '影视后期制作': 2, '待业': 538, '律师': 19, '律师助理': 8, '心理医生': 5,
                         '快递员': 4, '总监': 34, '总经理': 54, '总裁助理': 9, '房地产交易': 45, '房地产策划': 14, '投资': 55, '护士': 188, '招聘专员': 10, '招聘经理': 7, '摄影师': 8,
                         '撰稿人': 6, '操作工人': 152, '政府机构': 435, '教务管理人员': 136, '教授': 34, '教育/科研': 448, '文员': 181, '文案策划': 16, '景观设计': 14, '服务业': 498,
                         '未填写': 5256, '模特': 7, '法务专员': 4, '法务经理': 1, '法律': 28, '注册会计师': 4, '测试专员': 1, '渠道/分销专员': 33, '渠道/分销管理': 50, '演员': 12,
                         '物业管理': 18, '物料管理': 33, '物流/仓储': 29, '物流专员': 13,
                         '物流主管': 9, '物流经理': 25, '生产/制造': 176, '生产领班': 37, '生物/制药': 38, '生物工程': 11, '电子技术': 11, '画家': 4, '知识产权专员': 2, '科研人员': 22,
                         '科研管理人员': 10, '秘书': 18, '税务专员': 6, '税务经理': 1, '空乘人员': 4, '系统管理员': 4, '经理': 61, '经纪人': 1, '经销商': 222, '编辑': 32,
                         '网站产品经理': 8,
                         '网页设计': 20, '美容师': 265, '职业技术教师': 37, '自由职业': 2484, '舞蹈': 26, '药剂师': 64, '药品生产': 7, '营运主管': 13, '营运经理': 5, '规划师': 1,
                         '计算机/互联网': 107, '记者': 5, '讲师/助教': 116, '设计师': 76, '证券': 18, '财会/审计': 164, '财务主管': 80, '财务总监': 33, '财务经理': 38, '货运代理': 4,
                         '车间主任': 10, '运营管理': 74, '通信/电子': 53, '通信技术': 56, '酒店服务员': 34, '酒店管理': 76, '采购专员': 28, '采购经理': 18, '金融': 119,
                         '金融/银行/保险': 93,
                         '银行': 160, '销售': 886, '销售专员': 343, '销售主管': 283, '销售总监': 2456, '销售经理': 354, '集装箱业务': 3, '零售店店长': 62, '音乐家': 6, '项目主管': 33,
                         '飞行员': 3, '餐厅服务员': 50, '餐饮管理': 260,
                         '高级管理': 116}}

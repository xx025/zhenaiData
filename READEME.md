# 珍爱网征婚信息爬取和分析

# 注:此程序仅用于获得数据,分析数据请使用`zhenaiAnalyzeData/*`


## 分析: 
  1. 无论是城市和链接页面还是记录页面都有两种抓取方式,第一种是从`<body>`标签内第二种是`<script>`标签内  
  2. 获取城市及链接采用第一种,获取记录信息使用第二种
  3. 未登录用户只能查看每个城市的前6页大约120条,程序可搜索并爬取了所有城市(470个)近5600条左右
    

## 运行
1. 在运行之前需要搭建好`Mysql`数据库,并创建对应的表,sql语句在下面,对应的数据库账户和密码在`connectMysql/MYSQKJDBC`文件更改
2. 首先运行`Tools/getcitylist.py`获取页面链接并写入数据库`citylink`表
3. 再运行`GetMerberInfo.py`获取记录信息并写入数据库`memberdata`表
4. 重要!!,请在`connectMysql/MYSQKJDBC`对cookis进行填写

## 其他
1. 要注意的是,从获取数据到写入数据库都未改变对应的键和值  
    1. 那么性别列值1表示女性,值0表示男性
2. 对于反爬虫机制,程序设置了一定的时间间隔但仅有此是不足的,更多请更改`Tools.py`headers字典中的值,或进行代理访问 
3. 连接数据库请利用MySQLJDBC工具类
4. 由于程序具有时效性,项目创建时间2020-12-05
### 创建数据库和表格SQL语句

```sql
-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.27 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 zhenai0x2 的数据库结构
CREATE DATABASE IF NOT EXISTS `zhenai0x2` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `zhenai0x2`;

-- 导出  表 zhenai0x2.citylink 结构
CREATE TABLE IF NOT EXISTS `citylink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loc` varchar(32) DEFAULT NULL,
  `link` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=471 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。

-- 导出  表 zhenai0x2.memberdata 结构
CREATE TABLE IF NOT EXISTS `memberdata` (
  `age` int(11) DEFAULT NULL,
  `avatarURL` varchar(100) DEFAULT NULL,
  `car` varchar(8) DEFAULT NULL,
  `children` varchar(18) DEFAULT NULL,
  `constellation` varchar(16) DEFAULT NULL,
  `education` varchar(16) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `house` varchar(16) DEFAULT NULL,
  `introduceContent` text,
  `isRecommend` varchar(2) DEFAULT NULL,
  `lastModTime` varchar(32) DEFAULT NULL,
  `marriage` varchar(16) DEFAULT NULL,
  `memberID` varchar(16) DEFAULT NULL,
  `nickName` varchar(32) DEFAULT NULL,
  `objectAge` varchar(32) DEFAULT NULL,
  `objectHight` varchar(16) DEFAULT NULL,
  `objectMarriage` varchar(16) DEFAULT NULL,
  `objectSalary` varchar(32) DEFAULT NULL,
  `occupation` varchar(32) DEFAULT NULL,
  `salary` varchar(32) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `workCity` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

```
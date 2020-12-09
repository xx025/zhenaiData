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
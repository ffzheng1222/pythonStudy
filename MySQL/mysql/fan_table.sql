/*
Navicat MySQL Data Transfer

Source Server         : Tony
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : python_sql

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2020-05-11 17:21:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for fan_table
-- ----------------------------
DROP TABLE IF EXISTS `fan_table`;
CREATE TABLE `fan_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  `sex` varchar(100) NOT NULL,
  `score` int(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fan_table
-- ----------------------------
INSERT INTO `fan_table` VALUES ('1', 'tony', '18', '男', '89');
INSERT INTO `fan_table` VALUES ('2', 'Bob', '17', '男', '75');
INSERT INTO `fan_table` VALUES ('3', 'Mary', '18', '女', '92');
INSERT INTO `fan_table` VALUES ('4', 'John', '20', '男', null);
INSERT INTO `fan_table` VALUES ('5', 'Judy', '19', '女', null);



==========================================================================


-- 插入一行数据
INSERT INTO `fan_table` VALUE (1, 'tony', 18, '男', 89);
INSERT INTO `fan_table` VALUE (2, 'Bob', 17, '男', 75);

-- 插入多行数据
INSERT INTO `fan_table` VALUES (3, 'Mary', 18, '女', 92);
INSERT INTO `fan_table` (`name`, `age`, `sex`) VALUES
	('John', 20, '男'),
	('Judy', 19, '女')
;


-- 查询所有数据
SELECT * FROM `fan_table` ;

-- 查询fan_table表中所有的男生的指定信息，并倒序(DESC 倒序, ASC顺序--默认)输出
SELECT `id`, `name`, `age`, `sex` FROM 	`fan_table` WHERE `sex`='男' ORDER BY `id` DESC

-- 根据where条件更新数据
UPDATE `fan_table` SET `sex`='女' WHERE `sex`='男' ;
UPDATE `fan_table` SET `sex`='男' WHERE `score`>0 ;





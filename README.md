# weibo_top_spider数据爬虫
### 1.使用python3.9
### 2.框架Scrapy 2.4.1
### 3.数据保存到MySQL 5.6.16
### 4.数据定时一天更新一次
### 5.防止反爬使用代理
### 6.数据库脚本:
```sql
CREATE DATABASE /*!32312 IF NOT EXISTS*/`weibo_top` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `weibo_top`;

DROP TABLE IF EXISTS `weibo_top`;

CREATE TABLE `top` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `rank` int(11) DEFAULT NULL COMMENT '排名',
  `name` varchar(512) DEFAULT NULL COMMENT '名称',
  `tag` varchar(8) DEFAULT NULL COMMENT '标签',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_delete` tinyint(4) DEFAULT '0' COMMENT '是否删除：0否，1是',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

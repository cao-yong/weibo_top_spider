# import MySQLdb
import pymysql
from scrapy.utils.project import get_project_settings


class DBHelper:

    def __init__(self):
        # 配置在config.py中的数据库信息
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

    def connect_mysql(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               charset='utf8')
        return conn

    def connect_database(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')
        return conn

    def create_database(self):
        conn = self.connect_mysql()

        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    def create_table(self, sql):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    def insert(self, sql, *params):
        conn = self.connect_database()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def update(self, sql, *params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, sql, *params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()


class TestDBHelper:
    def __init__(self):
        self.dbHelper = DBHelper()

    def test_create_database(self):
        self.dbHelper.create_database()

    def test_create_table(self):
        sql = "CREATE TABLE `top` (" \
              "`id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键'," \
              "`rank` int(11) DEFAULT NULL COMMENT '排名'," \
              "`name` varchar(512) DEFAULT NULL COMMENT '名称'," \
              "`tag` varchar(8) DEFAULT NULL COMMENT '标签'," \
              "`create_time` datetime DEFAULT NULL COMMENT '创建时间'," \
              "`update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'," \
              "`is_delete` tinyint(4) DEFAULT '0' COMMENT '是否删除：0否，1是'," \
              "PRIMARY KEY (`id`)" \
              ") ENGINE=InnoDB DEFAULT CHARSET=utf8"
        self.dbHelper.create_table(sql)

    def test_insert(self):
        sql = "INSERT INTO `top`(`rank`,`name`,`tag`," \
              "`create_time`,`update_time`" \
              ") VALUES (%s,%s,%s,NOW(),NOW())"
        params = ("1", "金晨 贾乃亮", "沸")
        self.dbHelper.insert(sql, *params)

    def test_update(self):
        sql = "UPDATE `top` SET `rank`=%s,`name`=%s,`tag`=%s WHERE `id`='1'"
        params = ("2", "辽宁新增6例无症状 ", "沸")
        self.dbHelper.update(sql, *params)

    def test_delete(self):
        sql = "DELETE FROM `top`.`top_site`  WHERE `id`=%s"
        params = "1"
        self.dbHelper.delete(sql, *params)


if __name__ == "__main__":
    testDBHelper = TestDBHelper()
    #testDBHelper.test_insert()

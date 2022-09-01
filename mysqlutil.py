import pymysql as pymysql


class MysqlUtil:
    # 初始化函数
    def __init__(self, host, port, user, pwd, db, charset):
        # 连接mysql数据库
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=db, charset=charset)
        # 设置自动提交
        self.conn.autocommit(True)
        # 获取游标对象
        self.cursor = self.conn.cursor()

    # 查询
    def query(self, sql, param=None):
        # 执行sql语句
        self.cursor.execute(sql, param)
        # 获取查询数据
        return self.cursor.fetchall()

    def update(self, sql, param=None):
        try:
            # 执行语句
            self.cursor.execute(sql, param)
            # 提交
            self.conn.commit()
        except Exception as result:
            print(result)
            # 回滚
            self.conn.rollback()

    # 关闭函数
    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()


if __name__ == '__main__':
    mu = MysqlUtil(host='127.0.0.1', port=3306, user='root', pwd='root', db='waimai', charset='utf8')
    sql = 'select * from waimaiyuan where wid=%s' % '01001'
    name = "关羽"
    sql1 = 'select * from waimaiyuan where wname=%s' % '关羽'
    print(mu.query(sql))
    mu.close()

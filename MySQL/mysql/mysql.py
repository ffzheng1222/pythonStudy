import MySQLdb


class MySQLdbSearch(object):

    def __init__(self):
        self.get_connect()

    def get_connect(self):
        """
          获取数据库的连接
        """
        try:
            self.sql_connect = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='',
                db='python_sql',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error %s' % e)

    def close_connect(self):
        """
          关闭数据库的连接
        """
        try:
            if self.sql_connect:
                self.sql_connect.close()
        except MySQLdb.Error as e:
            print('Error %s' % e)

    def get_search_result_by_page(self, sql_cmd, page, page_size):
        """ 分页查询数据 """
        offset = (page - 1) * page_size
        search_condition = ('百家', offset, page_size)
        result = self.get_search_result(sql_cmd, search_condition)
        return result

    def get_search_result(self, sql_cmd, search_condition):
        """
            查找满足条件的数据
        """
        # 得到数据库 "管理员"
        cursor = self.sql_connect.cursor()
        # 执行SQL语句
        if search_condition:
            cursor.execute(sql_cmd, search_condition)
        else:
            cursor.execute(sql_cmd, ('百家',))

        # 拿到执行结果, 处理数据
        # sql_result = cursor.fetchall()
        sql_result = [dict(zip([k[0] for k in cursor.description], rows)) for rows in cursor.fetchall()]

        # 关闭 "管理员" 以及 数据库连接
        cursor.close()
        self.close_connect()
        return sql_result

    def insert_one_data(self, sql_cmd):
        """
            插入一条数据
        """
        # 受影响的行数
        row_count = 0
        cursor = None
        try:
            # 获取链接和cursor
            cursor = self.sql_connect.cursor()
            # 执行sql, 提交数据到数据库
            cursor.execute(sql_cmd, ('标题9', '/static/img/news/01.png', '新闻内容9', '推荐', 1))
            cursor.execute(sql_cmd, ('标题10', '/static/img/news/01.png', '新闻内容10', '推荐', 1))
            # 提交事务
            self.sql_connect.commit()

        except MySQLdb.Error as e:
            print('error')
            # 回滚事务
            self.sql_connect.rollback()

        # 执行最后一条SQL影响的行数
        row_count = cursor.rowcount
        # 关闭cursor和链接
        cursor.close()
        self.close_connect()
        # row_count > 0 表示成功
        return row_count > 0

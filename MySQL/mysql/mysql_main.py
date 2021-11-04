#!/usr/bin/python
# coding=utf-8

from .mysql import MySQLdbSearch
from .sql_orm import OrmMySQLTest


def search_mysql_by_page(mysql):
    # 准备SQL执行语句
    mysql_cmd = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC LIMIT %s, %s;'
    # 查询数据库信息
    exec_sql_result = mysql.get_search_result_by_page(mysql_cmd, 2, 3)
    for item in exec_sql_result:
        print(item)
        print('------------------------------------')


def search_mysql(mysql):
    # 准备SQL执行语句
    mysql_cmd = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
    # 查询数据库信息
    exec_sql_result = mysql.get_search_result(mysql_cmd)
    for item in exec_sql_result:
        print(item)
        print('------------------------------------')


def inserts_mysql(mysql):
    # 准备SQL执行语句
    mysql_cmd = (
        "INSERT INTO `news`(`title`,`image`, `content`, `types`, `is_valid`) VALUE"
        "(%s, %s, %s, %s, %s);"
    )
    # 插入数据到数据库
    exec_insert_state = mysql.insert_one_data(mysql_cmd)
    if exec_insert_state:
        print('insert_one_data： 插入数据成功')
    else:
        print('insert_one_data： 插入数据失败')


def operate_mysql():
    mysql = MySQLdbSearch()
    # search_mysql(mysql)
    search_mysql_by_page(mysql)
    # inserts_mysql(mysql)


def orm_inserts_mysql(orm_mysql):
    orm_result = orm_mysql.orm_insert_one_data()
    print(orm_result.id)


def orm_search_mysql(orm_mysql):
    orm_sch_results = orm_mysql.orm_get_search_result()
    for orm_sch_result in orm_sch_results:
        if orm_sch_result:
            print('ORM  ID:{0} ==> {1}'.format(orm_sch_result.id, orm_sch_result.title))
        else:
            print('Not exist!')


def orm_update_mysql(orm_mysql):
    orm_update_result = orm_mysql.orm_update_sql_data()
    print(orm_update_result)


def orm_delete_mysql(orm_mysql):
    orm_del_result = orm_mysql.orm_delete_sql_data()
    print(orm_del_result)


def operate_mysql_orm():
    orm_mysql = OrmMySQLTest()

    # 使用ORM给mysql数据库插入数据
    # orm_inserts_mysql(orm_mysql)

    # 使用ORM来查询mysql数据库中的数据
    # orm_search_mysql(orm_mysql)

    # 使用ORM来更新修改mysql数据库中的数据
    # orm_update_mysql(orm_mysql)

    # 使用ORM来删除mysql数据库中的数据
    orm_delete_mysql(orm_mysql)


def mysql_main():
    # operate_mysql()
    operate_mysql_orm()


if __name__ == '__main__':
    mysql_main()

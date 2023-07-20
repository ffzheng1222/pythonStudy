# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2022/4/9 0:00
# Author     ：p_fazheng
# version    ：python 3.8
# Description：
"""

import produce_script
import data_reduce

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_mysql import OrmMysqlOps
from pathlib import Path
from urllib import parse



# 读取已存manifest.yaml文件内的数据，写入mysql指定DB库表中
def write_mysql_from_manifest(mysql_ops):
    data_record_dict_list = data_reduce.data_reduce_main()
    for data_record_dict in data_record_dict_list:
        mysql_ops.orm_insert_odd_data(data_record_dict)
        # print(data_record_dict['checkpoint_name'])



#根据mysql DB库中的数据记录创建文件目录树
def create_file_tree_from_mysql(mysql_ops, **mcArgus):
    sql_select_cmd = "select category,product_name,component_name from " + \
        mcArgus['mysql_dbname'] + "." + mcArgus['mysql_db_table'] + \
        " group by category, product_name, component_name; "

    sql_res = mysql_ops.session.execute(sql_select_cmd)  # res是获取的对象
    select_data_record_list = sql_res.fetchall()  # data_record_list
    # print(select_data_record_list)
    for data_record_tuple in select_data_record_list:
        # 创建目录
        path = Path.cwd() / mcArgus['dir_tree_root_file'] / data_record_tuple[0] / data_record_tuple[1] / data_record_tuple[2]
        path.mkdir(parents=True, exist_ok=True)
        # print(path, path.exists())



# 根据mysql DB库中数据生成对应的script脚本文件
def generate_script_file_from_mysql(mysql_ops, mcArgus):
    #一次性读取数据库，做本地缓存
    all_source_data_records = list(mysql_ops.orm_get_all_record())
    all_data_records = all_source_data_records

    produce_script.produce_script_main(all_data_records, mcArgus)




# 创建mysql oam连接Session实例
def create_oam_mysql(**kwargs):
    mysql_address = kwargs['mysql_address']
    mysql_port = kwargs['mysql_port']
    mysql_user = kwargs['mysql_user']
    mysql_passwd = kwargs['mysql_passwd']
    mysql_dbname = kwargs['mysql_dbname']
    charset = 'utf8'

    #engine = create_engine("mysql://root:Tcdn@2007@10.2.200.139:3306/jumpserver?charset=utf8")
    mysql_passwd = parse.quote_plus(mysql_passwd)
    engine = create_engine("mysql://" +
                           mysql_user + ":" + mysql_passwd + "@" +
                           mysql_address + ":" + str(mysql_port) + "/" +
                           mysql_dbname + "?" + charset)
    # 返回的是类，创建与数据库的会话session类 ,这里返回给session的是个class,不是实例
    Session = sessionmaker(bind=engine)
    print("create_oam_mysql ...")
    return engine, Session


def main():
    # 测试产品名

    # mysql连接参数聚集 以及 各类配置参数
    mcArgus = dict()
    mcArgus['mysql_address'] = "9.134.160.37"
    mcArgus['mysql_port'] = 3306
    mcArgus['mysql_user'] = "mariadb_admin"
    mcArgus['mysql_passwd'] = "KneEb@3267MgUJ"
    mcArgus['mysql_dbname'] = "jumpserver"
    # mcArgus['mysql_address'] = "9.134.160.37"
    # mcArgus['mysql_port'] = 3306
    # mcArgus['mysql_user'] = "mariadb_admin"
    # mcArgus['mysql_passwd'] = "KneEb@3267MgUJ"
    # mcArgus['mysql_dbname'] = "jumpserver"
    mcArgus['mysql_db_table'] = "tcecli_checkpoint_tony"
    mcArgus['dir_tree_root_file'] = "destFile"

    # 1.创建mysql数据库连接
    Engine, Session = create_oam_mysql(**mcArgus)
    mysql_ops = OrmMysqlOps(Engine, Session)
    # mysql_ops.init_db()   #暂时不能用，有bug

    # 2.将已存在的manifest.yaml数据并入库
    write_mysql_from_manifest(mysql_ops)

    # 3.根据mysql DB库中的数据记录创建文件目录树
    create_file_tree_from_mysql(mysql_ops, **mcArgus)

    # 4.根据mysql DB库中的数据记录生成可用manifest.yaml 以及 各类cli工具脚本
    print("#####################################################")
    generate_script_file_from_mysql(mysql_ops,  mcArgus)

    # 5.关闭数据库连接
    Session().close()

if __name__ == '__main__':
    main()
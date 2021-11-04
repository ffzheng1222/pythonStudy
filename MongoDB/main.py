#!/usr/bin/python
# coding=utf-8

from mongodb.mongodb import TestMongoDB
from mongodb.odm_mongodb import TestMongoODM


def odm_mongodb_insert_data(odm_mongodb_obj):
    odm_mon_result = odm_mongodb_obj.odm_insert_data()
    print(odm_mon_result.pk)


def odm_mongodb_main():
    odm_mongodb_obj = TestMongoODM()

    # odm_mongodb_insert_data(odm_mongodb_obj)
    # odm_mongodb_select_data(odm_mongodb_obj)
    # odm_mongodb_update_data(odm_mongodb_obj)
    # odm_mongodb_delete_data(odm_mongodb_obj)


def mongodb_insert_data(mongoDB_obj):
    mon_result = mongoDB_obj.insert_data()
    print(mon_result.inserted_id)


def mongodb_select_data(mongoDB_obj):
    # mon_result = mongoDB_obj.select_data()
    # for item in mon_result:
    #     print(item["_id"])

    mon_result_oid = mongoDB_obj.select_data('5ebaac47f2d3a94595db0fe1')
    print(mon_result_oid)


def mongodb_update_data(mongoDB_obj):
    mon_result = mongoDB_obj.update_data()
    print(mon_result.matched_count)
    print(mon_result.modified_count)


def mongodb_delete_data(mongoDB_obj):
    mon_result = mongoDB_obj.delete_data()
    print(mon_result.deleted_count)


def main():
    mongoDB_obj = TestMongoDB()

    # mongodb_insert_data(mongoDB_obj)
    # mongodb_select_data(mongoDB_obj)
    # mongodb_update_data(mongoDB_obj)
    mongodb_delete_data(mongoDB_obj)

    # 使用ODM来操作mongodb数据库
    odm_mongodb_main()


if __name__ == '__main__':
    main()

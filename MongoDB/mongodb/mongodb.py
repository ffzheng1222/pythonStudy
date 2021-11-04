from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime


class TestMongoDB:

    def __init__(self):
        self.client = MongoClient()
        # student表示MongoDB的数据库名
        self.db = self.client['students']

    def insert_data(self):
        """ 新增数据 """
        post = {
            'name': 'tony',
            'age': 22,
            'sex': '男',
            'grade': 99,
            'created_at': datetime.now()
        }
        return self.db.students.insert_one(post)

    def select_data(self, oid=None):
        if oid is None:
            # 查询一条数据
            # return self.db.students.find_one()

            # 查询多条数据
            return self.db.students.find({'name': 'tony'})

        # 查询指定ID的数据
        obj = ObjectId(oid)
        return self.db.students.find_one({'_id': obj})

    def update_data(self):
        """ 修改数据 """
        # 修改一条数据
        # return self.db.students.update_one({'sex': 'female'}, {'$inc': {'age': 100}})

        # 修改多条数据
        return self.db.students.update_many({}, {'$inc': {'grade': 100}})

    def delete_data(self):
        # 删除一条数据
        # return self.db.students.delete_one({'name': 'tony'})
        # 删除多条数据
        return self.db.students.delete_many({'name': 'tony'})

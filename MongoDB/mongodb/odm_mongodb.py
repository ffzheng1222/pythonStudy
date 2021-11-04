from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from mongoengine import (connect, Document, EmbeddedDocument,
                         StringField, IntField, FloatField, DateTimeField, ListField,
                         EmbeddedDocumentField)

connect('students', host='mongodb://localhost/students')


class Grade(EmbeddedDocument):
    """ 学生的成绩 """
    name = StringField(required=True)
    score = FloatField(required=True)


SEX_CHOICES = (
    ('female', '女'),
    ('male', '男')
)


class Student(Document):
    """ 学生模型 """
    name = StringField(required=True, max_lenght=32)
    age = IntField(required=True)
    sex = StringField(required=True, choices=SEX_CHOICES)
    grade = FloatField()
    created_at = DateTimeField(default=datetime.now())
    grades = ListField(EmbeddedDocumentField(Grade))
    address = StringField()
    school = StringField()


class TestMongoODM(object):

    def odm_insert_data(self):
        """ 新增数据 """
        yuwen = Grade(
            name='语文',
            score=95
        )

        english = Grade(
            name='英语',
            score=89)

        stu_obj = Student(
            name='张三',
            age=21,
            sex='male',
            grades=[yuwen, english]
        )
        # stu_obj.test = 'OK'
        stu_obj.save()
        return stu_obj

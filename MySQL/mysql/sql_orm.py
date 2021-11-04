from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, Boolean

engine = create_engine("mysql://root:@127.0.0.1:3306/python_sql?charset=utf8")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class news(Base):
    """
        新闻类型
    """
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300))
    author = Column(String(20))
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


class OrmMySQLTest(object):

    def __init__(self):
        self.session = Session()

    def orm_insert_one_data(self):
        """ 添加数据 """
        new_obj = news(
            title="标题",
            content="内容",
            types="百家"
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def orm_get_search_result(self):
        """ 查询一条数据 """
        # orm_result = self.session.query(news).get(1)
        """ 查询多条数据 """
        # filter_by(is_valid=True) 等价于 filter(news.is_valid == 1)
        # orm_result = self.session.query(news).filter_by(is_valid=True)
        orm_result = self.session.query(news).filter(news.is_valid == 1)

        return orm_result

    def orm_update_sql_data(self, kp=None):
        # """ 更新一条数据 """
        # news_obj = self.session.query(news).get(kp)
        # if news_obj:
        #     news_obj.is_valid = 0
        #     self.session.add(news_obj)
        #     self.session.commit()
        #     return True
        # return False

        """ 更新多条数据 """
        news_obj_list = self.session.query(news).filter(news.is_valid < 1)
        if news_obj_list:
            for news_obj in news_obj_list:
                news_obj.is_valid = 1
                self.session.add(news_obj)
            else:
                print('orm_update_sql_data success.')
            self.session.commit()
            return True
        else:
            return False

    def orm_delete_sql_data(self, kp=None):
        # """ 删除一条数据 """
        # news_obj = self.session.query(news).get(kp)
        # if news_obj:
        #     self.session.delete(news_obj)
        #     self.session.commit()
        #     return True
        # return False

        """ 删除多条数据 """
        news_obj_list = self.session.query(news).filter(news.is_valid < 1)
        if news_obj_list:
            for news_obj in news_obj_list:
                self.session.delete(news_obj)
            else:
                print('orm_delete_sql_data success.')
            self.session.commit()
            return True
        else:
            return False

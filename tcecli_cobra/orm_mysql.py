"""
# File       : orm_mysql.py
# Time       ：2022/4/9 8:00
# Author     ：p_fazheng
# version    ：python 3.8
# Description：
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, func, exists, and_

# 生成orm基类
Base = declarative_base()


#tcecli_checkpoint表的类，表的结构，要先用类的形式写好这个表格
class TcecliCheckpoint(Base):
    """ tcecli 检查点 """
    __tablename__ = 'tcecli_checkpoint_tony'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)   #自增id
    category = Column(String(20), nullable=False, unique=True)  #脚本分类
    product_name = Column(String(50), nullable=False)           #产品类型
    component_name = Column(String(50), nullable=False)         #组件名
    checkpoint_name = Column(String(50), nullable=False)        #检查项名称
    severity = Column(String(255), nullable=False)              #影响级
    hosttype = Column(String(255), nullable=False)              #节点类型
    description = Column(String(500), nullable=True)            #检查点描述
    status = Column(String(50), nullable=True)                  #版本状态
    tag = Column(String(255), nullable=False)                   #高可用检测场景
    command_type = Column(String(255), nullable=False)          #脚本类型
    command_code = Column(String(500), nullable=False)          #脚本执行代码
    command_content = Column(Text, nullable=True)               #command func函数体
    create_time = Column(DateTime, nullable=False, default='CURRENT_TIMESTAMP')
    update_time = Column(DateTime, nullable=False, default='CURRENT_TIMESTAMP', onupdate=True)
    # 创建更新时间，对数据的更新进行记录
    # create_time = Column(DateTime, nullable=False, default='CURRENT_TIMESTAMP', server_default=func.now(), onupdate=func.now())   #自动记录创建时间，默认传default
    # update_time = Column(DateTime, nullable=False, default='CURRENT_TIMESTAMP', server_default=func.now(), onupdate=func.now())   #自动记录修改时间，默认传default


class OrmMysqlOps(object):

    def __init__(self, Engine, Session):
        self.session = Session()
        self.engine = Engine

    def init_db(self):
        Base.metadata.create_all(self.engine)

    def drop_db(self):
        Base.metadata.drop_all(self.engine)

    def orm_insert_odd_data(self, data_record_dict):
        """ 添加数据 """

        # 判断数据记录是否存在，如果存在则不插入
        result = self.session.query(TcecliCheckpoint).filter(and_(
            TcecliCheckpoint.category == data_record_dict['category'],
            TcecliCheckpoint.product_name == data_record_dict['product_name'],
            TcecliCheckpoint.component_name == data_record_dict['component_name'],
            TcecliCheckpoint.checkpoint_name == data_record_dict['checkpoint_name']
        )).all()
        if len(result) > 0:
            # print("Mysql insert odd data record exists.")
            return  False

        try:
            tcecli_checkpoint_obj = TcecliCheckpoint(
                category = data_record_dict['category'],
                product_name = data_record_dict['product_name'],
                component_name = data_record_dict['component_name'],
                checkpoint_name = data_record_dict['checkpoint_name'],
                severity = data_record_dict['severity'],
                hosttype = data_record_dict['hosttype'],
                description = data_record_dict['description'],
                status = data_record_dict['status'],
                tag = data_record_dict['tag'],
                command_type = data_record_dict['command_type'],
                command_code = data_record_dict['command_code'],
                command_content = data_record_dict['command_content'],
                create_time = data_record_dict['create_time'],
                update_time = data_record_dict['update_time'],
            )
            self.session.add(tcecli_checkpoint_obj)
            self.session.commit()
            print("Mysql insert odd data record success ^_^")
            return  True
        except self.session.Error as e:
            print("Mysql insert odd data record error %s" % e)
            # 回滚事务
            self.session.rollback()
            return False


    def orm_get_all_record(self):
        """ 得到所有数据 """
        orm_result = self.session.query(TcecliCheckpoint).filter().all()
        return orm_result

    def orm_get_one_record(self, record_index):
        """ 得到一条数据 """
        orm_result = self.session.query(TcecliCheckpoint).get(record_index)
        return orm_result

    def orm_search_odd_record(self, **search_cond):
        """ 根据条件查询单条数据 """
        search_field = search_cond['filed_name']
        search_value = search_cond['filed_value']

        orm_result = None
        if search_field == 'id':    #根据id查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.id == search_value)
        elif search_field == 'category':  #根据脚本分类查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.category == search_value)
        elif search_field == 'product_name':  #根据产品类型查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.product_name == search_value)
        elif search_field == 'component_name':  #根据组件名查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.component_name == search_value)
        elif search_field == 'severity':  #根据影响级查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.severity == search_value)
        elif search_field == 'hosttype':  # 根据节点类型查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.hosttype == search_value)
        elif search_field == 'status':  # 根据版本状态查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.status == search_value)
        elif search_field == 'tag':  # 根据高可用检测场景查找
            orm_result = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.tag == search_value)
        return orm_result

    def orm_search_more_record(self, **search_cond):
        """ 根据条件查询多条数据 """

        search_field = search_cond['filed_name']
        search_value = search_cond['filed_value']

        orm_result = None
        if search_field == 'id':  # 根据id查找
            orm_result = self.session.query(TcecliCheckpoint).filter(id=search_value)
        elif search_field == 'category':  # 根据脚本分类查找
            orm_result = self.session.query(TcecliCheckpoint).filter(category=search_value)
        elif search_field == 'product_name':  # 根据产品类型查找
            orm_result = self.session.query(TcecliCheckpoint).filter(product_name=search_value)
        elif search_field == 'component_name':  # 根据组件名查找
            orm_result = self.session.query(TcecliCheckpoint).filter(component_name=search_value)
        elif search_field == 'severity':  # 根据影响级查找
            orm_result = self.session.query(TcecliCheckpoint).filter(severity=search_value)
        elif search_field == 'hosttype':  # 根据节点类型查找
            orm_result = self.session.query(TcecliCheckpoint).filter(hosttype=search_value)
        elif search_field == 'status':  # 根据版本状态查找
            orm_result = self.session.query(TcecliCheckpoint).filter(status=search_value)
        elif search_field == 'tag':  # 根据高可用检测场景查找
            orm_result = self.session.query(TcecliCheckpoint).filter(tag=search_value)
        return orm_result


    def orm_update_odd_record(self, search_cond, update_record):
        """ 更新单条数据 """

        search_field = search_cond['filed_name']
        search_value = search_cond['filed_value']
        update_filed_name = update_record['filed_name']
        update_filed_value = update_record['filed_value']

        try:
            if search_field == 'id' and update_filed_name == 'id':  # 根据id更新数据记录
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.id == search_value).all()
                if tcecli_checkpoint_obj:
                    tcecli_checkpoint_obj.id = update_filed_value
                    self.session.add(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql update odd data record success by id ^_^")
                    return True
            elif search_field == 'product_name' and update_filed_name == 'product_name':  # 根据产品类型查找
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(TcecliCheckpoint.id == search_value).all()
                if tcecli_checkpoint_obj:
                    tcecli_checkpoint_obj.product_name = update_filed_value
                    self.session.add(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql update odd data record success by %s  ^_^" % search_field)
                    return True
            # TODO add
        except self.session.Error() as e:
            print("Mysql update odd data record error %s" % e)
            # 回滚事务
            self.session.rollback()
            return False


    def orm_delete_record(self, delete_cond):
        """ 根据条件删除数据 """

        delete_field = delete_cond['filed_name']
        delete_value = delete_cond['filed_value']

        try:
            if delete_field == 'id':  # 根据id删除
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(category=delete_value)
                if tcecli_checkpoint_obj:
                    self.session.delete(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql delete data record success by %s  ^_^" % delete_field)
                    return True
            elif delete_field == 'product_name':  # 根据产品类型删除
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(component_name=delete_value)
                if tcecli_checkpoint_obj:
                    self.session.delete(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql delete data record success by %s  ^_^" % delete_field)
                    return True
            elif delete_field == 'severity':  # 根据影响级删除
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(severity=delete_value)
                if tcecli_checkpoint_obj:
                    self.session.delete(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql delete data record success by %s  ^_^" % delete_field)
                    return True
            elif delete_field == 'hosttype':  # 根据节点类型删除
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(hosttype=delete_value)
                if tcecli_checkpoint_obj:
                    self.session.delete(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql delete data record success by %s  ^_^" % delete_field)
                    return True
            elif delete_field == 'status':  # 根据版本状态删除
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(status=delete_value)
                if tcecli_checkpoint_obj:
                    self.session.delete(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql delete data record success by %s  ^_^" % delete_field)
                    return True
            elif delete_field == 'tag':  # 根据高可用检测场景删除
                tcecli_checkpoint_obj = self.session.query(TcecliCheckpoint).filter(tag=delete_value)
                if tcecli_checkpoint_obj:
                    self.session.delete(tcecli_checkpoint_obj)
                    self.session.commit()
                    print("Mysql delete data record success by %s  ^_^" % delete_field)
                    return True
        except self.session.Error as e:
            print("Mysql delete data record error %s" % e)
            # 回滚事务
            self.session.rollback()
            return False
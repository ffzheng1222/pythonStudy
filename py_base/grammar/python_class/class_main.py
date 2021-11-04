from .student import Student
from .worker import Worker
from .person import Person


def set_object_info(name, st):
    if name is 'Tony':
        st.set_stu_info('星子一中', '高一二班', 680)
    elif name is 'Mary':
        st.set_stu_info('星子二中', '高一三班', 520)
    elif name is 'Bob':
        st.set_stu_info('星子三中', '高一五班', 490)


def init_class():
    name = "cao"
    worker1 = Worker(name)

    name = 'Tony'
    stu1 = Student(name, 'man', '--16')
    set_object_info(name, stu1)
    stu1.get_stu_info()

    name = 'Mary'
    stu2 = Student(name, 'woman', '17')
    set_object_info(name, stu2)
    stu2.get_stu_info()

    name = 'Bob'
    stu3 = Student(name, 'man', '18')
    set_object_info(name, stu3)
    stu3.get_stu_info()

    # print(stu1.__dir__())

    # worker1, stu1, stu2, stu3是已经实例化了的对象
    class_lists = [worker1, stu1, stu2, stu3]
    for class_obj in class_lists:
        p = Person(class_obj)
        p.do_func()


#### main program ###
if __name__ == '__name__':
    init_class()

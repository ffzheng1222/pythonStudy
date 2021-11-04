from .person import Person


class Student(Person):
    school = ''
    school_class = ''
    score = 0

    def __init__(self, name, gender, age):
        # 调用父类的构造方法
        # super().__init__(name, gender, age)
        # super().show_person_info()
        super().__init__()
        self.name = name
        self.gender = gender
        self.age = age

    def do_homework(self):
        print('%s work ...' % self.name)

    def do_func(self):
        self.do_homework()

    def set_stu_info(self, school, school_class, score):
        self.school = school
        self.school_class = school_class
        self.score = score

    def get_stu_info(self):
        super().show_person_info(self)
        print('%s studying %s at %s' %
              (self.name, self.school_class, self.school))
        print('\n')

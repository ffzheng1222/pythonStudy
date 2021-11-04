class Person:
    def __init__(self, obj=None):
        self.obj = obj

    def do_func(self):
        self.obj.do_func()

    @staticmethod
    def show_person_info(per_obj):
        print('%s is a %s , %s years old'
              % (per_obj.name, per_obj.gender, str(per_obj.age)))

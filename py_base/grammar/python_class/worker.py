from .person import Person


class Worker(Person):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def do_eat(self):
        print('%s eat ...' % self.name)

    def do_func(self):
        self.do_eat()

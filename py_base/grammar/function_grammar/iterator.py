class as_iterator:
    """
    迭代器用法1 (list tuple str 等可迭代对象)

    Version: 0.1
    Author: tonyfan
    """

    def __init__(self):
        self.use_while_true = True
        self.i_list = [2, 5, 8, 9]
        self.i_tuple = (1, 4, 7, 3, 5)

    def as_iterator_list(self):
        it_list = iter(self.i_list)

        # 此处要特别注意：迭代器it只能遍历一次，而且只能往前不会后退
        if self.use_while_true:
            while True:
                try:
                    print("it_list next(): %s" % next(it_list))
                except StopIteration:
                    print("it_list 迭代器已经遍历完成. \n")
                    return
        else:
            for it_x in it_list:
                print("it_list: %d" % it_x)

    def as_iterator_tuple(self):
        it_tup = iter(self.i_tuple)

        # 此处要特别注意：迭代器it只能遍历一次，而且只能往前不会后退
        if self.use_while_true:
            a = len(self.i_tuple)
            while a > 0:
                print("it_tup next(): %s" % next(it_tup))
                a = a - 1
            print("it_tup 迭代器已经遍历完成. \n")
        else:
            for it_tup_x in it_tup:
                print("it_tup: %d" % it_tup_x)


class my_as_iterator:
    """
    迭代器用法2 (自定义 可迭代对象 & 迭代器)

    Version: 0.1
    Author: tonyfan
    """

    def __init__(self):
        pass

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

def py_param_dect(a, b=5, c=10, *args, **kw):
    """
    python 参数(形参)说明

    Version: 0.1
    Author: tonyfan
    """
    # 位置参数 & 参数默认值
    print("%s + %s + %s = %d" % (str(a), str(b), str(c), a + b + c))
    print()

    # 可变参数
    args_list = []
    if args:
        for element in args:
            args_list.append(element)
        print("args: %s" % args_list)
        print()
    else:
        print("args: %s" % args_list)
        print()

    # 关键字参数
    if kw:
        print(kw.items())
        print(kw.keys())
        print(kw.values())
        print()
    else:
        print("kw关键字参数为{}")
        print()


def py_fanc_param():
    # 位置参数 & 参数默认值
    py_param_dect(3)
    py_param_dect(5, b=3, c=13)

    # 可变参数
    py_param_dect(1, 3, 5, 7, 9)

    # 关键字参数
    py_param_dect(1, 3, 5, 7, 9, name="tony", age=25)
    py_param_dect(2, name="cao", age=24)


def py_function_desc():
    # python 函数参数处理
    py_fanc_param()

    # 匿名函数 / 内联函数
    py_lambda()

    # 回调函数
    n = int(input('请输入正整数n：'))
    py_callback(n, factorial_callback)
    py_callback(n, sum_callback)


def py_lambda():
    """
    匿名函数 / 内联函数的用法

    Version: 0.1
    Author: tonyfan
    """
    add = (lambda x, y: x + y)
    print(add(2, 3))
    print(add('Hello', ' World!'))

    names = ['tony', 'cao', 'john', 'jack']
    name_sorted = sorted(names, key=lambda name: name.lower())
    print(name_sorted)


def py_callback(x, math_func):
    """
    回调函数的用法

    Version: 0.1
    Author: tonyfan
    """
    print("start run py_callback ...")
    math_func(x)


def factorial_callback(num):
    factorial_sum = 1
    for i in range(1, num):
        factorial_sum *= i
    print("%s! = %d" % (str(num), factorial_sum))


def sum_callback(num):
    sum = 0
    for i in range(1, num):
        sum += i
    print("1+...+%s = %d" % (str(num), sum))

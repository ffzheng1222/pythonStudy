"""
装饰器用法

Version: 0.1
Author: tonyfan
"""

import functools


# 此时function_info是一个被封装了的无参装饰器
def function_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kw)

    return wrapper


@function_info
def test_function_info(p):
    print(test_function_info.__name__ + " param: " + p)


# 此时function_info是一个被封装了的带参装饰器
def function_info_prams(text):
    def function_infos(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('decorator prams = {}'.format(text))
            return func(*args, **kw)

        return wrapper

    return function_infos


@function_info_prams("tony")
def test_function_info_prams(p):
    print(test_function_info.__name__ + " param: " + p)


# print_msg是闭包外围函数
def print_msg():
    msg = "I'm closure"
    msg1 = "I'm closure too"

    # printer是嵌套函数
    def printer():
        print(msg)
        print(msg1)

    return printer


def test1():
    # 这里获得的就是一个闭包
    closure = print_msg()
    # 输出 I'm closure
    print(closure())
    print(closure.__closure__)
    print(closure.__closure__[0].cell_contents)
    print(closure.__closure__[1].cell_contents)

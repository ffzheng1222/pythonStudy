"""
生成器用法

Version: 0.1
Author: tonyfan
"""


# 此时fibonacci是一个生成器函数
def fibonacci(n):
    a, b, count = 0, 1, 0
    while True:
        if count > n:
            return
        yield a
        a, b = b, a + b
        count += 1


def transfer_fibonacci():
    f = fibonacci(20)  # f 是一个迭代器，由生成器返回生成
    while True:
        try:
            print(next(f), end=', ')
        except StopIteration:
            return

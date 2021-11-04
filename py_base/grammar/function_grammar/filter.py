import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


def function_filter():
    # 过滤出1~100中平方根是整数的数：
    r = filter(is_sqr, range(100))
    print(list(r))

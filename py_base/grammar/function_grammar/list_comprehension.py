"""
列表推导式的用法

Version: 0.1
Author: tonyfan
"""


def as_list_comprehension():
    square_lists = [x ** 2 for x in range(20)]
    even_square_lists = [x ** 2 for x in range(20) if x % 2 == 0]
    odd_square_lists = [x ** 2 for x in range(20) if x % 2 == 1]
    print(square_lists)
    print(even_square_lists)
    print(odd_square_lists)

    exf_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    exf_even_square_lists = [j ** 2 for i in exf_lists for j in i if j % 2 == 0]
    print(exf_even_square_lists)

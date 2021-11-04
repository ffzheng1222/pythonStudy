from python_base import *
from python_for_while import *
from python_function import *
from python_class import class_main
from python_regular import regular_main
from python_json import json_main

import python_examples as pe
import function_grammar as fg


def study_python_app():
    pe.python_app_main.python_examples_app()


def study_python_base():
    """study python base"""
    # check_leap_year()
    # string_oprate()
    # team_transform()
    # personal_income_tax()
    # dice_game()


def study_python_for_while():
    """study for and while"""
    # for_n_factorial()
    # for_is_prime_num()
    # for_get_approximate_multiple()
    # for_print_triangle()
    # find_prefect_num()
    # find_prime()
    # get_multiplication_table()
    # craps_game()
    # input_fibonacci_seq()
    # for_guess_game()
    # judg_lily()
    # judg_palindrome()
    # yang_hui_triangle()


def study_python_function():
    """study function """
    # py_function_desc()


def study_python_func_grammar():
    """ 列表推导式 """
    # fg.list_comprehension.as_list_comprehension()

    """ 迭代器 """
    # # list tuple str等可迭代序列
    # stu_it = fg.as_iterator()
    # fg.iterator.as_iterator.as_iterator_list(stu_it)
    # fg.iterator.as_iterator.as_iterator_tuple(stu_it)
    #
    # # 自定义类为可迭代对象， 并制作为迭代器
    # my_it_class = fg.my_as_iterator()
    # my_it = iter(my_it_class)
    # while True:
    #     try:
    #         print("my_it next(): %s" % next(my_it))
    #     except StopIteration:
    #         print("my_it 自定义迭代器已经遍历完成. \n")
    #         break

    """ 生成器 """
    # fg.transfer_fibonacci()

    """ 装饰器 """
    # fg.test_function_info("I'm a param")
    # fg.test_function_info_prams("I'm a param too")
    # fg.test1()

    """ 函数式编程map, reduce, filter, sorted, zip """
    # fg.function_map()
    # fg.function_reduce()
    # fg.function_filter()
    # fg.function_sorted()
    fg.function_zip()

def study_python_calss():
    class_main.init_class()


def study_python_regular():
    regular_main.reg_main()


def study_python_json():
    json_main.json_python()
    json_main.python_json()


def main():
    # study_python_app()
    # study_python_base()
    # study_python_for_while()
    # study_python_function()
    study_python_func_grammar()
    # study_python_calss()
    # study_python_regular()
    # study_python_json()


#### main program ###
if __name__ == '__main__':
    main()

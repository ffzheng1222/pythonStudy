def function_sorted():
    old_list = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]

    # 利用key来排序
    new_list = sorted(old_list, key=lambda x: x[1])
    print(new_list)

    new_list = sorted(old_list, key=lambda x: x[1], reverse=True)
    print(new_list)

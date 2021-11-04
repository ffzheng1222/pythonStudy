def function_zip():
    my_list = [11, 12, 13]
    my_tuple = (21, 22, 23)
    new_iter = zip(my_list, my_tuple)
    print(list(new_iter))

    my_dic = {31: 2, 32: 4, 33: 5}
    my_set = {41, 42, 43, 44}
    new_iter1 = zip(my_dic, my_set)
    print(list(new_iter1))

    my_pychar = "python"
    my_shechar = "shell"
    new_iter2 = zip(my_pychar, my_shechar)
    print(list(new_iter2))

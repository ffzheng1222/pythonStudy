def square(x):
    return x ** 2


def function_map():
    list_x = [1, 2, 3, 4, 5, 6]
    list_y = [1, 2, 3, 4, 5, 6]
    r = map(square, list_x)
    print(list(r))

    # for map_x in r:
    #     print(map_x)

    r1 = map(lambda x, y: x ** y, list_x, list_y)
    print(list(r1))

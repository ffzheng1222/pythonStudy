from functools import  reduce

def function_reduce():
    r = reduce(lambda x,y: x+y, [x for x in range(10)], 0)
    print(r)
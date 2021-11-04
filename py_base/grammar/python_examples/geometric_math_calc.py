"""
功能：输入必要条件计算平面几何图形的周长和面积
   圆：               周长 2*π *r         面积 π*r^2
   长方形(正方形)：   周长 2*（a+b）     面积 a*b
   三角形：           周长 a+b+c          面积 (a*h)/2
   梯形：             周长 a+b+c+d        面积 （a+b）*h/2
   扇形：             周长 2r+L           面积 1/2LR        弧长 L＝2R＋nπR÷180
Version: 0.1
Author: tonyfan
Date: 2020-04-06
"""

import math


def print_cf(perimeter, area):
    print('周长: %.2f' % perimeter)
    print('面积: %.2f' % area)


def circle_calc():
    radius = float(input('请输入圆的半径：'))

    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    print_cf(perimeter, area)


def rectangle_calc():
    height = float(input('请输入矩形的长：'))
    width = float(input('请输入矩形的宽：'))

    perimeter = 2 * (height + width)
    area = height * width
    print_cf(perimeter, area)


def triangle_calc():
    """
    功能：判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-06
    """
    a = float(input('请输入三角形的边a：'))
    b = float(input('请输入三角形的边b：'))
    c = float(input('请输入三角形的边c：'))

    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        p = perimeter / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print_cf(perimeter, area)
    else:
        print('不能构成三角形')



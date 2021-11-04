from math import sqrt


def for_n_factorial():
    """
    输入非负整数n计算n!

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    n = int(input('请输入正整数n：'))
    result = 1
    for x in range(1, n + 1):
        result *= x
    print("%d! = %d" % (n, result))


def for_is_prime_num():
    """
    输入一个正整数判断它是不是素数

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    num = int(input('请输入一个正整数: '))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False

    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)


def for_get_approximate_multiple():
    """
    输入两个正整数计算最大公约数和最小公倍数

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    x = int(input('请输入正整数x:'))
    y = int(input('请输入正整数y:'))
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break


def for_print_triangle():
    """
    打印各种三角形图案

    *             *         *
    **           **        ***
    ***         ***       *****
    ****       ****      *******
    *****     *****     *********
    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < (row - i - 1):
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


def find_prefect_num():
    """
    找出1~9999之间的所有完美数
    完美数是除自身外其他所有因子的和正好等于这个数本身的数
    例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    for num in range(1, 10000):
        result = 0
        factor_list = []
        for factor in range(1, int(sqrt(num)) + 1):
            if num % factor == 0:
                result += factor
                factor_list.append(factor)
                if factor > 1 and (num // factor != factor):
                    result += num // factor
                    factor_list.append(num // factor)
        if num == result:
            print("%d is 完美数" % num)
            print(factor_list)
            print()


def find_prime():
    """
    输出2~99之间的素数

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    prime_list = []
    for num in range(2, 99):
        is_prime = True
        for x in range(2, int(sqrt(num)) + 1):
            if num % x == 0:
                is_prime = False
        if is_prime:
            prime_list.append(num)
    print(prime_list)


def get_multiplication_table():
    """
    输出乘法口诀表(九九表)

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """

    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='\t')
        print()


def craps_game():
    """
    Craps赌博游戏
    玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
    如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
    玩家再次摇色子 如果摇出7点 庄家胜
    如果摇出第一次摇的点数 玩家胜
    否则游戏继续 玩家继续摇色子
    玩家进入游戏时有1000元的赌注 全部输光游戏结束

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    from random import randint

    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True

        while needs_go_on:
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
                needs_go_on = False
            elif current == first:
                print('玩家胜')
                money += debt
                needs_go_on = False

    print('你破产了, 游戏结束!')


def input_fibonacci_seq():
    """
    输出斐波那契数列的前20个数
    1 1 2 3 5 8 13 21 ...

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    a = 0
    b = 1
    fibonacci_list = []
    for _ in range(50):
        a, b = b, a + b
        fibonacci_list.append(a)
    print(fibonacci_list)


def for_guess_game():
    """
    猜数字游戏
    计算机出一个1~100之间的随机数由人来猜
    计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    import random

    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')


def judg_lily():
    """
    找出100~999之间的所有水仙花数
    水仙花数是各位立方和等于这个数本身的数
    如: 153 = 1**3 + 5**3 + 3**3

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


def judg_palindrome():
    """
    判断输入的正整数是不是回文数
    回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    num = int(input('请输入一个正整数: '))
    temp = num
    num2 = 0
    while temp > 0:
        num2 *= 10
        num2 += temp % 10
        temp //= 10
    if num == num2:
        print('%d是回文数' % num)
    else:
        print('%d不是回文数' % num)


def yang_hui_triangle():
    """
    输出10行的杨辉三角 - 二项式的n次方展开系数
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    ... ... ...

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-19
    """
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

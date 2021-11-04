

def team_transform():
    """
    功能：将华氏温度转换为摄氏温度
    F = 1.8C + 32

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-06
    """
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))

    tc = float(input('请输入摄氏温度: '))
    tf = 1.8 * tc + 32
    print('%.1f摄氏度 = %.1f华氏度' % (tc, tf))


def string_oprate():
    """
    功能：字符串常用操作

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-06
    """
    str1 = "hello world!"
    print('字符串长度大小：', len(str1))
    print('单词首字母变大写：', str1.title())
    print('字符串变大写：', str1.upper())
    print('字符串是不是大写: ', str1.isupper())
    print('字符串是不是以hello开头: ', str1.startswith('hello'))
    print('字符串是不是以hello结尾: ', str1.endswith('hello'))
    print('字符串是不是以感叹号开头: ', str1.startswith('!'))
    print('字符串是不是一感叹号结尾: ', str1.endswith('!'))


def check_leap_year():
    """
    功能：输入年份 如果是闰年输出True 否则输出False

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-06
    """
    year = int(input('请输入年份: '))
    # 如果代码太长写成一行不便于阅读 可以使用\或()折行
    is_leap = (year % 4 == 0 and year % 100 != 0 or
               year % 400 == 0)
    print(is_leap)


def personal_income_tax():
    """
    功能：输入月收入和五险一金计算个人所得税
    说明：写这段代码时新的个人所得税计算方式还没有颁布

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-06
    """

    salary = float(input('本月收入: '))
    insurance = float(input('五险一金: '))
    diff = salary - insurance - 5000
    if diff <= 0:
        rate = 0
        deduction = 0
    elif diff < 1500:
        rate = 0.03
        deduction = 0
    elif diff < 4500:
        rate = 0.1
        deduction = 105
    elif diff < 9000:
        rate = 0.2
        deduction = 555
    elif diff < 35000:
        rate = 0.25
        deduction = 1005
    elif diff < 55000:
        rate = 0.3
        deduction = 2755
    elif diff < 80000:
        rate = 0.35
        deduction = 5505
    else:
        rate = 0.45
        deduction = 13505
    tax = abs(diff * rate - deduction)
    print('个人所得税: ￥%.2f元' % tax)
    print('实际到手收入: ￥%.2f元' % (diff + 5000 - tax))


def dice_game():
    """
    功能：掷骰子决定做什么事情

    Version: 0.1
    Author: tonyfan
    Date: 2020-04-06
    """
    from random import randint

    face = randint(1, 6)
    if face == 1:
        result = '唱首歌'
    elif face == 2:
        result = '跳个舞'
    elif face == 3:
        result = '学狗叫'
    elif face == 4:
        result = '做俯卧撑'
    elif face == 5:
        result = '念绕口令'
    else:
        result = '讲冷笑话'
    print(result)

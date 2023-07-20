# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : qsli_tool.py
# Time       ：2022/4/4 10:00
# Author     ：jokerxhshen
# version    ：python 3.7
# Description：
"""


import re


# 打开文件, 将内容存进内存.
def openFile(fileName):
    with open(fileName, 'r', encoding='UTF-8') as file:
        return file.readlines()


# 找到函数体, 并返回字符串Body.
# 只针对 function xxx() {} 标准定义shell定义函数, 其他格式失效.
def findFuncName(contentList, funcName):
    patternPre = "function.*"
    # 标志位, 是否找到函数名称. 默认为 false
    findFuncFlag = False
    for index, line in enumerate(contentList):
        # 去除文件行的左右空格. 注意会把 \n 换行符也去掉.
        line = line.strip()
        # 找到目标函数名称
        pattern = patternPre + funcName
        # 匹配是否包含 function funcName 字符串, 返回[funcName,]
        resultFuncA = re.findall(pattern, line)
        # 匹配开头是否包含注释.
        resultFuncB = re.findall(r'^#', line)
        # 如果找到了条件A, 且又不在注释行内:
        # print("1111 resultFuncA=%s  , resultFuncB=%s" % (resultFuncA,resultFuncB))
        if resultFuncA and not resultFuncB:
            findFuncFlag = True
            # 接着开始找 { , 并开始计数:
            return findFuncBody(contentList[index:])

        else:
            # 如果没找到 目标函数名称, 则开始下一行查找.
            continue

    # 对结果进行处理
    if not findFuncFlag:
        # 如果该文件没有找到目标函数名称, 则抛异常, 返回空字符串
        print("X111111111111111")
        raise ValueError("Can not find {} func, return nil".format(funcName))


# 找函数体, 并以字符串返回, 如果书写不规范, 则抛异常, 并返回nil
# 标准函数体定义
# function xxx() {
#   xxx
# }
def findFuncBody(contentList):
    braceNum = 0
    braceFlag = False
    resultList = []
    for line in contentList:
        # line 为函数开头行, 所以第一行一定 braceNum = 1
        if re.findall(r'{', line) and not re.findall(r'^#', line.strip()):
            braceNum = braceNum + 1
            braceFlag = True

        if re.findall(r'}', line) and not re.findall(r'^#', line.strip()):
            braceNum = braceNum - 1

        # 判断哪些文本行应该被提取.
        if braceNum == 0 and braceFlag:
            # 如果左右括号数量相等, 则表示函数体完毕, 跳出循环.
            # 把 } 所在行, 也加进结果所在函数体.
            resultList.append(line)
            break
        elif braceNum < 0:
            # 如果先于 '{' 之前, 找到了 '}', 则抛异常.
            raise ValueError("func: {} has bad definition, pls check func body.".format(funcName))

        elif braceNum > 0:
            # 如果该值大于0
            # 会把第一行, function xxx() { 也加进去.
            resultList.append(line)

    # 如果一直找不到函数的 { 起始括号
    # 则抛出异常, 对程序进行终止.
    if not braceFlag:
        raise ValueError("func: {} has bad definition, pls check func body.".format(funcName))

    return resultList


# 入口函数.
def entry(fileName, funcName):
    content_list = openFile(fileName)
    resultList = findFuncName(content_list, funcName)
    # resultStr为 function0 xxx() {} 定义文件头的完整字符串.
    resultStr = ''.join(resultList)
    # 对函数体内容进行截取.
    startAddrList = [substr.start() for substr in re.finditer(r'{', resultStr)]
    endAddrList = [substr.start() for substr in re.finditer(r'}', resultStr)]
    startAddr = startAddrList[0] + 1  # 左边位置为第一次出现 { 位置, 左闭右开, 所以左边 +1
    endAddr = endAddrList[-1]  # 左闭右开, 所以右边位置为最后一次出现 } 符号的位置.
    bodyStr = resultStr[startAddr:endAddr]
    return bodyStr


if __name__ == '__main__':
    # funcName = "check_hadoop_crontab_setup"
    # fileName = "text.txt"

    # funcName = "displayTpUsageStatement"
    # fileName = "hdfs_cli_360"

    bodyStr = entry(fileName, funcName)
    print(bodyStr)

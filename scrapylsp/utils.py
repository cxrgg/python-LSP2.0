# 引入模块
import os
import re


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False


# 切割字符串:去除中[]及其中间的所有值
def subBrackets(name):
    pattern = r'\[.*?\]'
    return re.sub(pattern, '', name)


# 获取url最后一个/前面的值
def subUrlBefore(name):
    pattern = r'/([^/]+).html'
    return re.sub(pattern, '', name) + "/"


# 获取url最后一个/后面的值
def subUrlAfter(name):
    return re.split("/", name)[-1]

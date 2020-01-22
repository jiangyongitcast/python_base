import os

dir1 = '中国近代史 马克思主义基本原理 高等数学工本 Java语言程序设计一 ' \
       'C++语言程序设计 数据结构 数据库系统原理 计算机系统结构 操作系统 ' \
       '软件工程 计算机网络原理 概率论和数理统计二 英语二 离散数学'

dir2 = '历年考题 电子书 Code 教程 学习笔记'

list1 = dir1.split()
list2 = dir2.split()


def mkdir1():
    for i in range(0, len(list1)):
        os.mkdir(str(i + 1) + list1[i])
        for j in range(0, len(list2)):
            os.mkdir('./' + str(i + 1) + list1[i] + '/' + str(j + 1) + list2[j])


if __name__ == '__main__':
    # print(list1)
    mkdir1()
    pass
# os.mkdir("高等教育")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
from notebook.notebookapp import raw_input
import os
# str=raw_input("请输入：")
# print("您输入的内容为"+str)
#
# str=input("请输入具体内容：")
# print("具体内容为"+str)

# file = open("hello.txt", "w+", 1)
# # 获取文件名
# print(file.name)
#
# print(file.mode)
# file.write("www.runoob.com")
#
# red = open("hello.txt", "r+")
# st = red.read(10)
# print("读取的字符串为：" + st)
#
# position = red.tell()
#
# print("当前位置为："+str(position))
# # 关闭文件
# red.close()
# os.renames("hello.txt", "hu.txt")
# # os.remove("hu.txt")
# try:
#     fh = open("hello", "r")
#     fh.write("这是一个测试文件，用于测试异常！")
# except IOError:
#     print("Error: 没有找到文件或者读取文件失败")
# else:
#     print("内容写入成功")
#     fh.close()
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print("Error: 没有找到文件或读取文件失败")

# #这是一行搞笑的注释
# name = input('enter your name:')
# print('hello,',name)


#数据类型和变量
#整数 0x十六进制 浮点数 科学计数法1.23*10^9=1.23e9 整数运算永远是精确的，/和//地板除
#浮点数有四舍五入的误差


# # 字符串 ‘’ “” ‘abc’ "I'm OK"
# # 转义字符 \  'I\'m \"OK\"!'   \n \t \\
# print('I\'m ok.')
# print("I'm ok.")
# print('I\'m learning\nPython.')
# print('\\\n\\')
# # 为了解决频繁使用\造成的代码阅读障碍，用r''表示''内部的字符串默认不转义
# print('\\\t\\')
# print(r'\\\t\\')
# # '''...'''表示多行内容
# print('''line1
# line2
# line3''')
# print(r'''line1
# line2
# line3''')
# print(r'''hello,\n
# world''')


#布尔值 一个布尔值只有True、False两种
#>>>True
#True
# >>>False
# False
# >>>3>2
# True
# >>>3>5
# False
#布尔运算and/or/not

#空值None

#变量
# a = 123
# print(a)
# a = 'ABC'
# print(a)

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# n = 123
# f = 456.789
# s1 = 'Hello,world'
# s2 = 'Hello,\'Adam\''
# s3 = r'Hello,"Bart"'
# s4 = r'''Hello,
# lisa!'''
# print(n,f,s1,s2,s3,s4)

#字符编码  ASCII——unicode——UTF-8 
#计算机内存中统一使用Unicode，当需要保存到硬盘或者传输的时候，转换为UTF-8
#python的字符串
# print('包含中文的str')#python3字符串以unicode编码，支持多语言

# ord('A')  #ord获取字符的整数表示
# ord('中')
# chr(66)   #chr把编码转换成对应的字符
# chr(25991)

# '\u4e2d\u6587'  #十六进制

# x = b'ABC'  #bytes类型数据b''  b""   python字符串类型str，内存中以unicode表示，传输或保存，需把str变为以字节为单位的bytes
#'ABC'str   b'ABC'bytes每个字符占用一个字节

# 'ABC'.encode('ascii')#以Unicode表示的str通过encode()方法可以编码为指定的bytes
# '中文'.encode('utf-8')
#'中文'.encode('ascii')
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
#在bytes中，无法显示为ASCII字符的字节，用\x##显示。

#从网络或磁盘读到的数据是bytes。要把bytes变为str，就需要用decode()方法
# b'ABC'.decode('ascii')
# b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#b'\xe4\xb8\xad\xff'.decode('utf-8')#如果bytes中包含无法解码的字节，decode()方法会报错
# b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')

# len('ABC')
# len('中文')  #len()函数计算的是str的字符数
# len(b'ABC')
# len(b'\xe4\xb8\xad\xe6\x96\x87')#换成bytes，len()函数就计算字节数
# len('中文'.encode('utf-8'))

#!/usr/bin/env python3    告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-    告诉Python解释器，按照UTF-8编码读取源代码

#格式化  %d整数 %f浮点数 %s字符串 %x十六进制整数
# 'Hello,%s' % 'world'
# 'Hi,%s,you have $%d' % ('Michael',1000000)
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
# 'Age:%s. Gender:%s' % (25,True)
# 'growth rate:%d %%' % 7   #转义，用%%来表示一个%
# 'Hello,{0},成绩提高了{1:.1f}%'.format('小明',17.125)#字符串的format()方法，用传入的参数依次替换字符串内的占位符{0}、{1}……
# s1 = 72 
# s2 = 85
# r = (s2-s1)/s1*100
# print('{0}成绩提高了{1:.1f}%'.format('小明',r))

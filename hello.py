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

n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello,"Bart"'
s4 = r'''Hello,
lisa!'''
print(n,f,s1,s2,s3,s4)
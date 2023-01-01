# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:18:00 2022

@author: xhy
"""


# class revealAccess:

#     def __init__(self, initval=None, name='var'):

#         self.val = initval
#         self.name = name

#     def __get__(self, obj, objtype):

#         print("Retrieving", self.name)
#         return obj.val

#     def __set__(self, obj, val):

#         print("updating", self.name)
#         obj.val = val


# class myClass:

#     x = revealAccess(10, 'var "x"')
#     y = 5

#     def __init__(self):
#         self.x = 20


# # m = myClass()
# # print(m.val)
# # m.x = 15
# # print(m.x)
# # print(m.y)


class CLanguage:
    
    name1=45
    
    # 构造函数
    def __init__(self, name):
        self.name1 = name
    # 设置 name 属性值的函数

    def setname(self, name):
        self.name1 = name
    # 访问nema属性值的函数

    def getname(self):
        return self.name1
    # 删除name属性值的函数

    def delname(self):
        del self.name1

    name = property(getname, setname, delname, '指明出处')


clang = CLanguage("C语言中文网")
# 调用 getname() 方法
def getname(self):
    
    print("i am here")


# CLanguage.getname=getname

print(CLanguage.getname(clang))
# print(clang.name1)
# 调用 setname() 方法
clang.name = "Python教程"
# print(clang.name)
# 调用 delname() 方法


# CLanguage.name=10

# clang.name="p"



# # CLanguage.setname = 10
# print(clang.name1)

# # clang.setname=30

# clang.name="c++"

# print(CLanguage.setname)

# print(clang.name)

# python=CLanguage("python学习")
# print(python.name)
# # del clang.name
# # print(clang.name)

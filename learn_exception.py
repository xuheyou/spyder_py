# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:56:41 2023

@author: xhy
"""
def abc():
    
    try:
        a = int(input("请输入 a 的值:"))
        print(20/a)
        # raise
        print("ret 后")
    except:
        # raise
        print("发生异常！")
        
    else:
        print("执行 else 块中的代码")
    finally:
        # raise
        print("执行 finally 块中的代码")


abc()
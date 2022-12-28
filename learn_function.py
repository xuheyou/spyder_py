# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:18:05 2022

@author: xhy
"""


def str_max(str1, str2):
    '''
    比较两个字符串，返回最大的字符串

    Parameters
    ----------
    str1 : str
        字符串.
    str2 : str
        字符串.

    Returns
    -------
    str
        字符串.

    '''
    return str1 if str1 > str2 else str2


my_str = str_max("i love you", "you love me")
print(my_str)


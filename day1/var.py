# -*- coding:utf-8 -*-  # python3默认使用utf-8，这句可以省略
"""
Created on 2018/2/5
@Author: Jeff Yang
"""

name = "Jack"
name2 = name  # name2不是指向name而是指向name的值"Jack"

print("My name is ", name)

print(name, name2)

name = "Tom"  # 只有name变了，name2不会变

print(name, name2)

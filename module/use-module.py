#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'wei sheng gao'

import sys

def test():
    args = sys.argv
    print(args)
    # 第一项是执行文件的绝对路径
    # ['/Users/shenggao/Documents/code/python/module/use-module.py']
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s!' % args[1])
    else:
        print('too many arguments!')

# _开头的是 private 私有函数
# 外部不需要引用的函数全部定义成 private，只有外部需要引用的函数才定义为 public。
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__=='__main__':
    test()
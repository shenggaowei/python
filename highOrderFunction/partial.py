#! /usr/bin/env python3
import functools

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

# int 默认字符串参数认为是十进制，并转化成十进制的数字
print(int('12345'))

# int base=8 默认字符串参数认为是八进制，并转化成十进制的数字
print(int('12345', base=8))

# int base=16 默认字符串参数认为是十六进制，并转化成十进制的数字
print(int('12345', base=16))

def int2(x, base=2):
    return int(x, base)
print('int2', int2('1000000'))

_int2 = functools.partial(int, base=2)
print('_int2', _int2('1000000'))
print('_int2', _int2('1010101'))

kw = { 'base': 2 }
# 关键字参数
int('10010', **kw)

# 实际上会把10作为*args的一部分自动加到左边，也就是： args = (10, 5, 6, 7)
max2 = functools.partial(max, 10)
print('max2', max2(3,4,5,11))
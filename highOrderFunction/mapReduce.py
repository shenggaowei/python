#! /usr/bin/env python3
from functools import reduce

# map 返回一个 iterator，需转换成 list，打印出全部
operateL = list(map(str, [1,2,3,4,5]))
print(operateL)

# reduce
def add(sum, item):
    return sum + item;
sum = reduce(add, [1,2,3])
print(sum)

# 将 1,3,5,7,9 变成数字 13579
def fn(x, y):
    return x * 10 + y;
num = reduce(fn, [1,3,5,7,9,2]) 
print(f'num is {num}')

# 将字符串转成int
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
num2 = reduce(fn, map(char2num, '1357901'))
print(f'char2num is {num2}')

def str2Int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    return reduce(fn, map(char2num, s))
print('12123', str2Int('12123'))

def str2IntLambda(s):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print('121234', str2IntLambda('121234'))

# 首字母大写
def normalize(name):
    return name.capitalize();

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 计算乘积
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 字符串转浮点数
def str2float(s):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    def str2Int(x, y):
        return x * 10 + y;

    def str2Digital(x):
        length = len(str(x))
        return x / (10 ** length) 

    [num1, num2] = s.split('.') 
    return reduce(str2Int, map(char2num, num1)) + str2Digital(reduce(str2Int,map(char2num, num2)))

# 456
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
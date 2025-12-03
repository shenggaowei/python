#! /usr/bin/env python3

# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

def is_odd(n):
    return n % 2 == 1
# filter返回值为 iterable
ret = list(filter(is_odd, [1,2,3,4,5]))
print(ret)

# 筛选非空字符串
def not_empty(s):
    return s and s.strip()
ret2 = list(filter(not_empty, ['1', '2' ,None,'',' '])) 
print(ret2)

# 获取素数列表

# 定义奇数列表
def get_odd_list():
    n = 1;
    while True:
        n = n + 2
        yield n

# 定义 filter 过滤
def _not_divisible(n):
    return lambda x: x % n != 0

def prisma():
    yield 2
    # 初始序列
    it = get_odd_list()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in prisma():
    if n < 100:
        print(n)
    else:
        break;

# 回文序列 12321 
def is_palindrome(n):
    s = str(n)
    # 反转字符串
    return s == s[::-1] 

ret = filter(is_palindrome, range(1, 1000))
print(list(ret))
#! /usr/bin/env python3

ret = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(ret)

def f(x):
    return x * x

f2 = lambda x: x * x
print(f2)

def build(x,y):
    return lambda: x*x + y*y

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

L2 = list(filter(lambda n:n % 2 == 1, range(1,20)))

print(L)

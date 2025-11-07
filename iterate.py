#! /usr/bin/env python3

d = { 'a': 1, 'b': 2, 'c': 3 }
L = [2, 3, 4, 'ahha']

for value in L:
    print(value)

for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

for i,value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1,1), (2,4), (3,9)]:
    print(x, y)

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for value in L:
        if min >= value:
            min = value
        if max <= value:
            max = value
    return (min, max) 

# 测试
if findMinAndMax([]) != (None, None):
    print('1: 测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2: 测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3: 测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4: 测试失败!')
else:
    print('测试成功!')
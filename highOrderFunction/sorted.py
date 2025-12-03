#! /usr/bin/env python3

# 默认从大到小排
print(sorted([36, 5, -12, 9, -21]))

# sorted 为高阶函数，可传递处理函数
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按照名字进行排序
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

# 按照分数从大到小排序
def by_score(t):
    return -t[1]

L3 = sorted(L, key=by_score)
print(L3)
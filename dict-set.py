#! /usr/bin/env python3

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d['Michael'])
print(d.get('Bob'))

# 判断 key 是否存在
print('Michael' in d)

print(d.pop('Tracy'))

a = set((1, [2, 3]))
print(a)
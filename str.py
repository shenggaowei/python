#!/usr/bin/env python3

# 格式化 %
print('%d-%02d' %(3,1))
print('%.4f' %(3.14159267))
print('growth rate %d %%' %7)

# format
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

s1 = 72
s2 = 85
r = ((s2 - s1) / s1) * 100
print(f'{r:.2f}%')
print('%.2f%%' % r)
print('{0:.2f}%'.format(r))

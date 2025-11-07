#! /usr/bin/env python3

# 思路，取到第一个非空字符的下标和最后一个非空字符的下标，截取两个下标中间的字符

def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-2]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('1：测试失败!')
elif trim('  hello') != 'hello':
    print('2：测试失败!')
elif trim('  hello  ') != 'hello':
    print('3：测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4：测试失败!')
elif trim('') != '':
    print('5：测试失败!')
elif trim('    ') != '':
    print('6：测试失败!')
else:
    print('测试成功!')
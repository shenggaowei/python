#! /usr/bin/env python3

# 思路
# 先去除前空格，然后反转字符串，再去除前空格，再反转字符串。比较暴力

# 去除前空格
def trimPreWhiteSpace(s):
    s1='';
    length = len(s);
    c=0
    isNotNull = False
    while c < length:
        if s[c] == ' ' and isNotNull == False:
            pass
        else:
            s1 = s1 + s[c]
            isNotNull = True
        c = c + 1
    return s1

# 反转字符串
def reverseStr(s):
    s1 = '';
    sLength = len(s);
    while sLength > 0:
        index = sLength - 1
        s1 = s1 + s[index]
        sLength = sLength -1 
    return s1

def trim(s):
    #去除前空格
    s1 = trimPreWhiteSpace(s)
    #反转字符串
    reverseS1 = reverseStr(s1)
    #去除反转后的前空格
    s2 = trimPreWhiteSpace(reverseS1)
    #反转字符串
    s3 = reverseStr(s2)
    return s3

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

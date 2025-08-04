#!/usr/bin/env python3
age = 3;
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if 条件的隐式转换
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = (1,);
if x:
    print(True);
else:
    print(False);

# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
# 如果输入的是 'abc'，不是合法的数字时会报错，程序会退出。如何捕获错误呢？
birth = input('birth: ')
if int(birth) < 2000:
    print('00前');
else:
    print('00后');

# bmi 计算
height = 1.75
weight = 80.5

bmi = 80.5 / (1.75 * 1.75);
print(f'{bmi:.2f}')

if bmi < 18.5:
    print('过轻');
elif bmi >= 18.5 and bmi < 25:
    print('正常');
elif bmi >= 25 and bmi < 32:
    print('肥胖');
else:
    print('严重肥胖');
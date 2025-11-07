#! /usr/bin/env python3
# 切片 python 操作字符串没有相关的截取函数，只有切片的操作

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'];

# 取前三项
print(L[0:3])
print(L[:3])

# 取第2、3项
print(L[1:3])

# 取倒数第2个、倒数第1个元素
# 倒数第一个元素是 -1。正数第一个元素是 0
print(L[-2:-1])

L2 = list(range(100))
# 前10个数
print(L2[:10])
# 后10个数
print(L2[-10:])
#前11-20个数
print(L2[10:20])
#前10个数，每两个取一个
print(L2[:10:2])
#所有数，每5个取一个
print(L2[::5])

# 复制一个 list
print(L[:])

# tuple list
print((0,1,2,3,4,5)[:3])

# 字符串也可作为一个 list
print('ABCDEF'[:3])
print('ABCDEF'[::2])


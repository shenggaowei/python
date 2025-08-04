#!/usr/bin/env python3
classMates = ['m', 'b', 't'];
length = len(classMates)
print(classMates,'\n', length);

# 列表后添加元素
classMates.append('c');
print(len(classMates),'\n', classMates);

# 中间插入元素
classMates.insert(1, 'jack')
print('中间插入元素',classMates);

# 删除列表尾的元素
lastEle = classMates.pop()
print('删除最后一个元素',lastEle, classMates)

# tuple 元组。tuple 一旦初始化后就不能修改
classMateTuple = ('m', 'b', 't')
print(classMateTuple);

t = ();
print('t', t)

t = (1);
print('t', t)

t = (1,);
print('t', t)
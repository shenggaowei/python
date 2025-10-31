#! /usr/bin/env python3

#"计算x的平方"
def power(x):
    return x * x;

print('power(15)',power(15));

#"求x的n次方"
def powerN(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print('powerN(2,3):', powerN(2,4));

#"添加END到列表末尾 L在函数定义的时候值就被绑定计算出来了"
#"默认参数必须指向不变对象"
def add_end(L = []):
    L.append('END')
    return L
print('add_end():', add_end()); "['END']"
print('add_end():', add_end()); "['END', 'END']"
"正确写法"
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print('add_end():', add_end()); "['END']"
print('add_end():', add_end()); "['END']"

#给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print("calc", calc([1,2,3]))

#"可变参数"
#"*numbers 得到的 numbers 是个 tuple"
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum;
print('calc2', calc2(1,2,3))
print('calc2', calc2(*[1,2,3]))

#"关键字参数"
#"**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。"
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw);
extra={'city': 'Beijing', 'job': 'Engineer'}
person('Michael', 30, city='Beijing', job='Engineer')
person('Jack', 24, **extra)

#"命名关键字参数"
def person2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other', kw)
person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

#"关键字参数限制"
#"和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。"
def person3(name, age, *, city, job):
    print(name, age, city, job)
person3('Jack', 24, city='Beijing', job='Engineer')
person3('Jack', 24, city='Beijing', job='Engineer' ) 
#"TypeError: person3() got an unexpected keyword argument job2. Did you mean job"

def person4(name, age, *args, city, job):
    print(name, age, args, city, job);
#person4('Jack', 24, 'Beijing', 'Engineer')

def person5(name, age, *, city='Beijing', job):
    print(name, age, city, job);
person5('Jack', 24, job='Engineer')

def mul(*args):
    sum = 1
    for n in args:
        sum = sum * n
    return sum
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
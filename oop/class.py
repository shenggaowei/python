#! /usr/bin/env python3

# 类名首字母需要大写，object表示继承的类
class Student(object):
    # __init__ 相当于 constructor
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    # 第一个参数默认为 self，调用的时候不用传
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C' 

lisa = Student('lisa', 80)
bob = Student('bob', 90)

print(lisa.name, lisa.score)
print(bob.name, bob.score)

lisa.score = 81;

# 外部代码还是可以自由地修改一个实例的name、score属性：
print(lisa.name, lisa.score)
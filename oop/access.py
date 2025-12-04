#! /usr/bin/env python3

# 类名首字母需要大写，object表示继承的类
class Student(object):
    # __init__ 相当于 constructor
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def set_score(self, score):
        if not isinstance(score, int): 
            raise TypeError('bad operand type')
        self.__score = score
    
    def get_score(self):
        return self.__score
    
    # 第一个参数默认为 self，调用的时候不用传
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C' 

lisa = Student('lisa', 80)
bob = Student('bob', 90)

print(lisa._Student__name, lisa._Student__score)
print(bob._Student__name, bob._Student__score)

lisa.set_score(100)
print(lisa._Student__score)

# 外部代码还是可以自由地修改一个实例的name、score属性：
# print(lisa.name, lisa.score)
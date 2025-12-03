#! /usr/bin/env python3
import time, functools

def now():
    print('2024-06-01')
f = now
f()
# 函数名字
print(now.__name__)
print(f.__name__)

def log(func):
    # *args 是可变参数 **kw 是关键字参数
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now3():
    print('2024-06-01')
now3()

def log2(text):
    def decorator(func):
        # 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute')
def now5():
    print('2026-06-01')
now5()
# __name__ 由 now5 变成了 wrapper, 添加 @functools.wraps(func) 后，可变回 now5
print(now5.__name__)

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        startTime = time.time()
        ret = fn(*args, **kw)
        endTime = time.time()
        duration = (endTime - startTime) * 1000
        print('%s executed in %s ms' % (fn.__name__, duration))
        return ret
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def log3(fn):
    if fn == 'execute':
        def decorator(fn2):
            @functools.wraps(fn2)
            def wrapper(*args, **kw):
                print('%s begin call' % fn)
                ret = fn2(*args, **kw) 
                print('%s end call' % fn)
                return ret
            return wrapper
        return decorator
    else:
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('begin call')
            ret = fn(*args, **kw) 
            print('end call')
            return ret
        return wrapper
        

@log3('execute')
def f():
    return 1

f()
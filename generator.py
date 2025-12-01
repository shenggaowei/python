#! /usr/bin/env python3

L = [ x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))

for n in g:
    print(n)

def fib(max):
    n, a, b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done';

fib(6)


def fib(max):
    n, a, b = 0,0,1
    while n < max:
        yield b 
        a,b = b,a+b
        n = n + 1
    return 'done';
fib(6)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value：', e.value)
        break
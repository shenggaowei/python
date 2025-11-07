#! /usr/bin/env python3

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1);

#print(fact(100))

def fact2(n, sum = 1):
    if n==1:
        return sum 
    return fact2(n-1, sum * n);
print(fact2(100))

L = [];
n = 1;
while n <= 99:
    L.append(n)
    n = n + 2;
print(L)
#! /usr/bin/env python3

print(list(range(1,11)))

L = []
for x in range(1,11):
    L.append(x * x)
print(L)

L1 = [x * x for x in range(1,11)]
print(L1)
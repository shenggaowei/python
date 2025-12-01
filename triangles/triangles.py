#! /usr/bin/env python3

def triangles():
    data = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(1)
        data.append(row)
    
    for i in range(9):
        for j in range(9):
            # 第一项和最后一项都是1
            if j != 0 and j < i:
                data[i][j] = data[i-1][j] + data[i-1][j-1]
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i >= j:
                print('%6d' %(data[i][j]), end = " ")
        print('\n')

triangles()
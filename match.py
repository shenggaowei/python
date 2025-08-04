#!/usr/bin/env python3

score = 'B';
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

age = 25
match age:
    case x if x < 10:
        print(f'< 10 years old: {x}');
    case 10:
        print('10 years old');
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

args = ['gcc', 'hello.c', 'world.c', 'hello.cc']
match args:
    case ['gcc']:
        print('gcc: missing source file(s).')
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    case ['clean']:
        print('clean');
    case _:
        print('invalid command.')
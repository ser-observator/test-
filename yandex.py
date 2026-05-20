#!/usr/bin/env pnthon3
#a=int(input())
#b=int(input())
#c=int(input())
#if a<b+c and b<c+a and c<a+b:
#    print ('YES')
#else: print ('no')
stroka, stolbec, mina = map(int, input().split())

matrix = [[0] *stolbec for _ in range(stroka)]

for _ in range(mina):
    r,c= map(int, input().split())
    matrix[r-1][c-1]='*'







for row in matrix:
    print (' '.join(map(str, row)))
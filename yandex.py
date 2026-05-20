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
    r, c= map(int, input().split())
    matrix[r-1][c-1]='*'
    
for r in range(stroka):
        for c in range(stolbec):
            if matrix[r][c] == '*':
                continue
    
        count=0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if 0 <= r +dr < stroka and 0 <= c + dc < stolbec:
                    if matrix[r+dr][c+dc] == '*':
                        count +=1                    
        matrix[r][c]= count

for row in matrix:
    print (' '.join(map(str, row)))
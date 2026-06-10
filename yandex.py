#!/usr/bin/env pnthon3
#a=int(input())
#b=int(input())
#c=int(input())
#if a<b+c and b<c+a and c<a+b:
#    print ('YES')
#else: print ('no')



#stroka, stolbec, mina = map(int, input().split())
#
#matrix = [[0] *stolbec for _ in range(stroka)]
#
#for _ in range(mina):
#    r, c= map(int, input().split())
#    matrix[r-1][c-1]='*'
#    
#for r in range(stroka):
#    for c in range(stolbec):
#        if matrix[r][c] == '*':
#            continue
#    
#    
#    
#        count=0
#        for dr in [-1, 0, 1]:
#            for dc in [-1, 0, 1]:
#                if 0 <= r +dr < stroka and 0 <= c + dc < stolbec:
#                    if matrix[r+dr][c+dc] == '*':
#                        count +=1                    
#        matrix[r][c]= count
#
#for row in matrix:
#    print (' '.join(map(str, row)))




#def search(N):
#    R=(bin(N))[2:]
#    suma=0
#    for _ in R:
#        suma+=int (_)
#    if suma % 2==0:
#        New_R= '11'+R
#    else:
#        New_R= R+ '00'
#    r = int(New_R, 2)
#    return r
#for N in range(1,100):
#    r=search(N)
#    if r>116:
#        print(f'N={N}')
#        break

#def suma(N):
#    a=N//100
#    b= (N//10)%10
#    c=N%10
#    sum1= a+b
#    sum2= b+c
#    if 1<= sum1 <= 9 and 1<=sum2<=9:
#        r=str(sum1)+str(sum2)
#        return int(r)
#    return None 
#for N in range(100,999+1):
#    result= suma(N)
#    if result is not None:
#        print (f'N={N}, Результат ={result}')
#        break
#
#N=23
#N=(bin(N))[2:]
#suma=0
#for _ in N:
#    suma+=int (_)
#if suma % 2 ==0:
#    New_N= '10'+N
#else:
#    New_N = '1'+N
#n= int(New_N,2)
#print(n)






#https://education.yandex.ru/ege/inf/task/998fbc59-2d80-4b1c-9ac4-6b6386b090ed
#ебись нахуй
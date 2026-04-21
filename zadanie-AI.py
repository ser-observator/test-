#!/usr/bin/env pnthon3
#1 Работа с пременой
a=str(input("ваше имя: "))
b=int(input('ваш возраст: '))
if b<=1:
    c=str('год')
elif b<=4:
    с= str('года')
else:
    c= str("лет")
print (f'{a} исполниться будет {b+1} {c} в следующим году')

#3 Цикл for
#for i in range(1,10+1):
#    a=7
#    c=a*i
#    print(a, '*', i, '=', c)


#!/usr/bin/env pnthon3

# Задание 1: Работа со строками
#name=input('имя= ')
#print (f'Прив,{name}!')

 # Задание 2: Простые арифметические операции
a=int(input('a='))
b=int(input('b='))
c=input('операция= ')
if c=='+':
    print (a + b)
elif c=='-':
    print (a - b)
elif c== '//':
    print (a//b)
elif c== '%':
    print (a%b)
elif c== '*':
    print (a*b)
elif c== '**':
    print (a**b)
if c == '/' and b==0:
    print ('НЕВОЗМОЖНО')
#!/usr/bin/env pnthon3

#1 Работа с пременой
#a=str(input("ваше имя: "))
#b=int(input('ваш возраст: '))
#if b<=1:
#    c=str('год')
#elif b<=4:
#    с= str('года')
#else:
#    c= str("лет")
#print (f'{a} исполниться будет {b+1} {c} в следующим году')

#2 условные переменые if/else
#a=int(input ('введи число: '))
#if a % 2:
#    print('не чётное')
#else:
#    print ('чётное')

#3 Цикл for
#for i in range(1,10+1):
#    a=7
#    c=a*i
#    print(a, '*', i, '=', c)

#4 цикл while
#import random
#secret=random.random(1,10) #само загадное число до 10 (нейронка исправила до 10)
#number=0
#while secret !=number:
#    number= int(input('введи чесло, чтобы угадать(целые): '))
#    if number<secret:
#        print('не угадал, но малое')
#    elif number>secret:
#        print('не угадал, но большое')
#print('а хотя нет, угадал')

#5 Списки (List)
#fruits=['aplle', 'banan', 'cherry', 'perra', 'coffe beans']
#for fruit in fruits:
#    print (fruit)
#fruits.append('mango')
#print (f'{fruits} новый в списке')

#6 Словари (Dictionary) - сложно (списал)
#
#a= {
#    'Имя': 'Андрей',
#    'Возраст': 20,
#    'Оценка': (4),
#}
#for keys, value in a.items():
#    print(f'{keys}: {value}')

#7. Функции
#a=int(input('a='))
#b=int(input('b='))
#def sum(a,b):
#    return a+b
#result= sum(a,b)
#print(result)

# 8 Функция с проверкой
#number= int(input('простое ли число: '))
#def simple():
#    if number <2:
#        return False
#    for i in range(2, int( number**0.5)+ 1 ):
#        if number % i == 0:
#            return False
#    else:
#        return False
#print(simple())

#9 Обработка списков
#list=input('список чисел(через пробел): ')
#number= [int(x) for x in list.split()]
#print(list)
#print (f'максиальное:{max(number)}')
#print (f'минимальное:{min(number)}')
#print (f'среднее:{sum (number)}/{len (number)}')

#10  Строки (String)
str(input('запиши слово: '))

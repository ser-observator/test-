#https://education.yandex.ru/ege/inf/task/a5a6fe7c-3e0b-4e9c-9dbf-10560a973262
#сделано 222, но нужно ещё считать
#from turtle import *
#speed(1)
#screensize(1500, 1500)
#
#k=10
#lt(90)
#
#for _ in range(2):
#    fd(5 *k)
#    rt(90)
#    fd(11 * k)
#    rt(90)
#
#pu()
#bk(4*k)
#rt(90)
#fd(6*k)
#lt(90)
#
#pd()
#for _ in range(2):
#    fd(42*k)
#    rt(90)
#    fd(63*k)
#    rt(90)
#exitonclick()

#https://education.yandex.ru/ege/inf/task/a9b4ee81-7aca-4fca-9eec-1801673d12f2

from turtle import *
tracer(0)
speed(0)
screensize(150,150)
k=20
lt(90)

rt(45)
for _ in range(7):
    forward(5*k)
    rt(45)
    forward(10*k)
    rt(135)
penup()

for x in range(-20,20+1):
    for y in range(-20,20+1):
        setpos(x*k,y*k)
        dot(5, 'red')
exitonclick()

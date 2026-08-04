#https://education.yandex.ru/ege/inf/task/da9b8fa5-490a-48c5-a9c2-542e3343c920
#print ('a b c d F')
#for a in range (0,2):
#    for b in range (0,2):
#        for c in range (0,2):
#            for d in range (0,2):
#                F=int(((a and b)<= c) and ((b and c)<= d))
#                if F == 0:
#                    print (a, b, c, d, F)
#решено dbac

#https://education.yandex.ru/ege/inf/task/4c7c38c7-48e1-4428-af23-8ebbf2fbd088
#from itertools import product
#print ("x y z w F")
#for x, y, z, w in product(range(0,2), repeat=4):
#    F=int(((x and y) <= (not z))and (x <= y)or w)
#    if F==0:
#        print (x, y, z, w, F)
#решено xzwy

#https://education.yandex.ru/ege/inf/task/a0a0262b-ffa0-4fdb-a501-894d30e26aa9
#from itertools import product
#print ('x y w z F')
#for x,y,w,z in product(range(0,2), repeat=4):
#    F=int(((1==w)==(not((w and x)or y))) <= z)
#    print (x, y, w, z, F)
#решено xzyw

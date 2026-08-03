#!/usr/bin/env pnthon3
from itertools import product
print ('k n m h')
for k,n,m,h in product (range(2), repeat=4):
        if (((k and not m) or (n<=h))==(h==k))==True:
                print(k, n, m, h)
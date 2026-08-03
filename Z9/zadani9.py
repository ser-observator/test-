count = 0
for line in open('/home/obs/doc/python_and_informatika/test-/Z9/zadani9.txt'):
    a = [int(x) for x in line.split()]
    S= sum(a)
    C1 = S % 2 == 0 and any(a[i] + a[j] == S //2 
                                for i in range(4) for j in range (i+1, 4))
    C2 = max(a) < sum(a) - max(a)
    C3 = sum(a) % 2 == 0
    if C1 and C2 and C3:
        count +=1
print (count)
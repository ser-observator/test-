count = 0
for line in open("input.txt"):
    a = [int(x) for x in line.split()]
    p1= (a[0]+a[1])
    p2= (a[2]+a[3])
    if p1 == p2:
        count += 1
    l = max(a) < 
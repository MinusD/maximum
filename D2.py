c = 0
for i in range(1, 1000):
    n=1
    s=i
    while s<10:
        s*=2
        n*=5
    if n==125:
        c+=1
        print(i, c)

for i in range(1000):
    n = i
    s = 1
    while s<1000:
        s*=2
        n-=2
    if n ==100:
        print(i)

for i in range(1,1000):
    n = 1
    s = i
    while s<256:
        s*=2
        n*=3
    if n == 81:
        print(i)

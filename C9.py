for i in range(1, 1000):
    n = i
    s = 1
    while s<500:
        s*=2
        n+=9
    if n == 101:
        print(i)

for i in range(1000):
    s = i
    n = 0
    while s + n < 400:
        s-=5
        n+=20
    if n == 340:
        print(i)

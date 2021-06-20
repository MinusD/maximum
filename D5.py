for i in range(1000):
    s = 100
    n = i
    while s>=0:
        s-=10
        n+=20
    if n == 242:
        print(i)

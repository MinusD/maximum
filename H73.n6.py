for i in range(1, 1000):
    s = i
    s //= 10
    n = 1
    while n<=2000:
        n*=3
        s+=12
    if s == 115:
        print(i)

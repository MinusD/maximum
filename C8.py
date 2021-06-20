for i in range(1000):
    s = i
    n=1
    while n<=150:
        s+=30
        n*=5
    if s == 199:
        print(i)

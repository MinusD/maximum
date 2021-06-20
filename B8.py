for i in range(1000):
    n = 126
    s = i
    while s<=225:
        s+=8
        n-=5
    if n == 91:
        print(i)

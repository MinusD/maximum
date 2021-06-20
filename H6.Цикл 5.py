for i in range(100, 1000):
    x = i
    l = x - 15
    m = x + 20
    while l!=m:
        if l>m:
            l-=m
        else:
            m-=l

    if m == 35:
        print(i)

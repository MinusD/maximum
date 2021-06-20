for i in range(100, 1000):
    x = i
    l = x - 30
    m = x + 30
    while l!=m:
        if l>m:
            l-=m
        else:
            m-=l

    if m == 30:
        print(i)

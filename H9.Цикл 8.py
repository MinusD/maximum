for i in range(100, 1000):
    x = i
    l = x
    m = 77
    if l%2 == 0:
        m = 60
    while l!=m:
        if l>m:
            l-=m
        else:
            m-=l
    if m == 20:
        print(i)

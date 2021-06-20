for i in range(80, 1000):
    x = i
    l = x
    m = 55
    if l%2 ==0:
        m = 44
    while l!=m:
        if l>m:
            l-=m
        else:
            m-=l
    if m == 22:
        print(i)

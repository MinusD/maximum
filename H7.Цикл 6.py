for i in range(50, 1000):
    x = i
    l = x
    m = 35
    if l%2 ==0:
        m = 28
    while l!=m:
        if l>m:
            l-=m
        else:
            m-=l
    if m == 14:
        print(i)

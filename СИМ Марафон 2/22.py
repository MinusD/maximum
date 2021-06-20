for i in range(101, 1000):
    x=i
    l=2*x-40
    m = 2*x+40
    while l!=m:
        if l > m:
            l-=m
        else:
            m-=l
    if m == 40:
        print(i)

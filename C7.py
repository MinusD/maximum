for i in range(1000):
    s = i
    n=20
    while s*s*s<153:
        s+=1
        n+=3
    if n == 29:
        print(i)

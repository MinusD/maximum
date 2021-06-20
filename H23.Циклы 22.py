for i in range(-100, 100):
    s = i
    n = 0
    while s*s < 99:
        s+=1
        n+=2
    print(i, n)

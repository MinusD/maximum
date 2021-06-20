for i in range(100000):
    x = i
    a = 0
    b = 10
    while x>0:
        c=x%2
        a+=c
        if c == 0:
            a+=1
        else:
            b+=1
        x//=10
    if a == 2 and b == 3:
        print(i)
    print(i, a, b)

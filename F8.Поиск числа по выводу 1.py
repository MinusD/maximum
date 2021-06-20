for i in range(1000):
    x = i
    a = 0
    b = 10
    while x>0:
        c=x%10
        a+=c
        if c<b:
            b=c
        x//=10
    if a == 14 and b == 6:
        print(i)

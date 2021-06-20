for i in range(1000):
    x = i
    a = 1
    b = 0
    while x>0:
        if x%2 > 0:
            a*=x%6
        else:
            b+=x%6
        x//=6
    if a == 9 and b == 4:
        print(i)

for i in range(1, 1000):
    x = i
    a = 0
    b = 1
    while x > 0:
        if x%2 != 0:
            a+=x%8
        else:
            b*=x%8

        x//=8
    if a == 3 and b == 8:
        print(i)

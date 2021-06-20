for i in range(1000):
    x = i
    a = 0
    b = 1
    while x>0:
        if x%2 > 0:
            a+=1
        else:
            b*=x%4
        x//=4
    if a == 2 and b == 0:
        print(i)

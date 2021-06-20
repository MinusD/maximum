for i in range(1000):
    x = i
    r = 0
    n = 0
    while x>0:
        d=x%7
        r+=d
        x//=7
        n+=1
    if r == 13 and n == 3:
        print(i)

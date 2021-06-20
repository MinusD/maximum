for i in range(1000):
    x = i
    r = 0
    n = 0
    while x>0:
        d = x % 3
        r+=d
        x//=3
        n+=1
    if r==6 and n == 4:
        print(i)

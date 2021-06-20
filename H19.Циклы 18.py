for i in range(1000):
    x = i
    l = 0
    m = 0
    while x>0:
        m+= x%8
        if x%2 == 0:
            l+=1
        x//=8
    if l == 2 and m == 20:
        print(i)

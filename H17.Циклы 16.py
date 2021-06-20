for i in range(1000):
    x = i
    l = 0
    m = 0

    while x>0:
        m+=1
        if x%2 ==0:
            l+=x%6
        x//=6
    if l==10 and m == 3:
        print(i)

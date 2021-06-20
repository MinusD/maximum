for i in range(1000):
    x = i
    l = 0
    m = 0
    while x>0:
        m+=1
        if x%2 !=0:
            l+=1
        x//=2
    if l == 4 and m == 7:
        print(i)

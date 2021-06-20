for i in range(1000):
    x = i
    q = 8
    l = 0
    while x >= q:
        l+=1
        x-=q
    m = x
    if m < l:
        m = l
        l = x
    if l == 4 and m == 6:
        print(i)

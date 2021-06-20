for i in range(1000):
    x = i
    q = 7
    l = 0
    while x >= q:
        l+=1
        x-=q
    m = x
    if m < l:
        m = l
        l = x
    if l == 2 and m == 3:
        print(i)

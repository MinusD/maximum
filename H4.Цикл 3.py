for i in range(1000):
    x = i
    q = 11
    l = 0
    while x >= q:
        l+=1
        x-=q
    m = x
    if m < l:
        m = l
        l = x
    if l == 0 and m == 7:
        print(i)

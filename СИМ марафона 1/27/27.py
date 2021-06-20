with open('27-B.txt', 'r') as f:
    n = int(f.readline())
    b = []
    for i in range(5):
        b.append(int(f.readline()))
    mp = 1000*1000+1
    m2 = 1001
    m = 1001
    for i in range(5, n):
        m = min(b[0], m)
        m2 = min(b[0], m%2*1001+m)
        x = int(f.readline())
        p = m2*x
        if x%2==0 and m*x < p:
            p = m*x
        if p < mp and p%2 == 0:
            mp = p
        for j in range(4):
            b[j] = b[j+1]
        b[4] = x
    if mp == 1000*1000+1:
        mp = -1
    print(mp)

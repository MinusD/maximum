#27-2
with open('27-3.txt') as f:
    k = int(f.readline())
    m = 0
    d = []
    for i in range(10):
        d.append(int(f.readline()))
    m = sum(d)
    
    s = f.readline()
    while s!= '':
        del d[0]
        d.append(s)
        m = max(sum(d), m)
    print(m)
        
        

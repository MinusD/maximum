with open('24.txt', 'r') as f:
    st = f.readline()
    st = '3369633303301516'
    a = list(st)
    c = 1
    m = 0
    for i in range(1, len(a)):
        if int(a[i-1])%3 == 0 and int(a[i])%3 == 0 and int(a[i-1])!=0 and int(a[i]) != 0:
            c+=1
            m = max(m, c)
        else:
            c = 1
    print(m)

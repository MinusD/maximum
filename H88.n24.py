with open('24.txt', 'r') as f:
    st = f.readline()
    counter = 1
    m = 1
    for i in range(1, len(st)):
        if st[i-1].isdigit() and st[i].isdigit():
            if int(st[i-1]) <= int(st[i]):
                counter +=1
                m = max(m, counter)
            else:
                counter = 1
        else:
            counter = 1
    print(m)
    

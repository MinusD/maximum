with open('27-C.txt', 'r') as f:
    n = int(f.readline())
    a = []
    counter = 0
    d43 = 0
    for i in range(5):
        a.append(int(f.readline()))
    for i in range(n-5):
        if a[0]%43 == 0:
            counter += n-5-i
        print(a)
        print(a[0])
        del a[0]
        a.append(int(f.readline()))    
    print(counter)

with open('27-B.txt', 'r') as f:
    n = int(f.readline())
    a = []
    counter = 0
    d43 = 0
    for i in range(5):
        a.append(int(f.readline()))
    for i in range(5, n):
        if a[0]%43 == 0:
            d43 +=1
        x = int(f.readline())
        if x%43 == 0:
            counter+=i-4
        else:
            counter+=d43
        del a[0]
        a.append(x)    
    print(counter)

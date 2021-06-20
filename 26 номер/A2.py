with open('4.txt', 'r') as f:
    tmp = f.readline().split()
    n = int(tmp[0])
    s = int(tmp[1])
    a = []
    for i in range(n):
        a.append(int(f.readline()))
    a.sort()
    a = a[:s]
    sum = 0
    for i in a:
        sum += i 
    print(max(a), sum/len(a))

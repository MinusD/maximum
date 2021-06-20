with open('1A.txt', 'r') as f:
    rr = []
    sum = 0
    n = int(f.readline())
    for i in range(n):
        tmp = f.readline().split()
        rr += max(tmp)
        print(tmp, rr)

f = open('27-B.txt')
nn = int(f.readline())
n77 = 0
n11 = 0
n7 = 0
n0 = 0
for i in range(nn):
    n = int(f.readline())
    if n%77 == 0:
        n77 = max(n77, n)
    if n%11 == 0:
        n11 = max(n11, n)
    if n%7 == 0:
        n7 = max(n7, n)
    n0 = max(n0, n)
f.close()
print(max(n77*n0, n11*n7))
print(n77, n11, n7, n0)
        

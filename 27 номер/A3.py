f = open('3B.txt')
n = int(f.readline())
n3 = 0
n5 = 0
for i in range(n):
    a = int(f.readline())
    if a % 3 == 0 and a != n3 and a>n3:
        n3 = a
    elif a % 5 == 0 and a != n5 and a>n5:
        n5 = a
print(n3*n5)
f.close()
        

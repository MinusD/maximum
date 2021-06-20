f = open('26.txt')
tmp = f.readline().split()
s = int(tmp[0])
n = int(tmp[1])
a = []
sm = 0
c = 0
for i in range(n):
    a.append(int(f.readline()))

for i in range(n):
    m = min(a)
    if sm + m <=s:
        sm+=m
        c+=1
        a.remove(m)
    else:
        break
print(c, sm)

f.close()

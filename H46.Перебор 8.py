n = 0
m = 100000
for i in range(7543, 11524):
    dd = i%2
    ddd = i%6
    if i%9 == 0 and dd != ddd:
        n+=1
        mi = i
        m = min(m, i)
print(m, n)

n = 0
m = 100000
for i in range(13213, 20412):
    s = i//10
    if i%4 == 0 and ((s%10 + i%10) > 10):
        n+=1
        mi = i
        m = min(m, i)
print(n, mi)

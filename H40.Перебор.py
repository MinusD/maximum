n = 0
for i in range(1101, 9515):
    if i%9==0 and i%7!=0 and i%15!=0 and i%17!=0 and i%19!=0:
        n+=1
        m = i
print(n, m)

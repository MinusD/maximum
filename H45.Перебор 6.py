n = 0
m = 100000
for i in range(1113, 3513):
    s = i//10
    if i%10!=0 and i%10!=3 and i%10!=5 and i%10!=7 and not(s%10==1 and i%10==4):
        n+=1
        mi = i
        m = min(m, i)
print(n, m)

n = 0
m = 100000
for i in range(1097, 13762):
    if i%2==0 and i%7!=0 and i%11!=0 and i%13!=0 and i%31!=0:
        n+=1
        m = min(m, i)
print(n, m)

n = 0
m = 0
for i in range(11111, 20001):
    if (i%2 == 0) and (i%3==0) and (i%7!=0) and (i%11!=0) and (i%13!=0) and (i%10 == 4):
        n+=1
        m = max(m, i)
print(n, m)
        

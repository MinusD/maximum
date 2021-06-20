m = 0
n = 0
for i in range(129, 4500):
    if i%3 == 0 and i%10 == 3:
        if i%4!= 0 and i%6!= 0 and i%9 != 0 and i%9 != 0:
            n += 1
            m+=i
print(n, m/n)
                
            

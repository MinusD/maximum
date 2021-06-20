m = 1016000
n = 0
for i in range(2854, 15715):
    if i%6 == 0 and i%9 == 0:
        if i%8!= 0 and i%12!= 0 and i%15 != 0:
            if i < m:
                m = i
            n += 1
print(n, m)
                
            

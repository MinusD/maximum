c = 0
m = 99999
for i in range(3072, 7321):
    if i%10==5 and (i%7==0 or i%11==0 or i%13 ==0):
        c+=1
        m = min(m, i)
print(c, m)


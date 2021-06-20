n = 0
m = 100000
for i in range(127, 5279):
    if i%7==0 and i%11!=0 and i%19!=0 and i%23!=0 and i%10==1:
        mi = i
        m = min(m, i)
print(mi - m, mi+m)

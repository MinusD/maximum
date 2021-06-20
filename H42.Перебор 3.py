n = 0
m = 100000
for i in range(5422, 11664):
    if i%3==0 and i%5==0 and i%9!=0 and i%13!=0 and i%17!=0:
        n+=1
        mi = i
        m = min(m, i)
print(m, mi)

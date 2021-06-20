m = 0
n = 0
for i in range(896, 9885):
    if i%4 == 0 and i%7 ==0:
        if i%9!= 0 and i%15!= 0 and i%19 != 0:
            if i > m:
                m = i
            n += 1
print(n, m)

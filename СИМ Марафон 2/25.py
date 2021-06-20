a = []
for i in range(513125, 554886):
#for i in range(2, 100):
    s = sum([int(nu) for nu in str(i)])
    if s%5==0:
        de = 0
        for j in range(2, i//2+1):
            if i%j==0:
                de = 1
                break
        if de == 0:
            a.append([i, s])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

m = 1016000
n = 0
for i in range(1869, 9870):
    if i%4 == 0:
        if i%3!= 0 and i%5!= 0 and i%6 != 0 and i%12 != 0:
            if i < m:
                m = i
            n += 1
print(n, m)

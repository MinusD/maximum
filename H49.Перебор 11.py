from random import *
n = int(input('Количество чисел: '))
minsum = 20000
a = [randint(1, 1000) for i in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        minsum = (min(minsum, a[i] + a[j]) if (a[i] + a[j])%2 == 0 else minsum)
print(minsum)

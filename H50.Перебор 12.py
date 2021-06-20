from random import *
n = int(input('Количество чисел: '))
answer = 0
a = [randint(1, 1000) for i in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        answer += (1 if (a[i] + a[j])%14 == 0 else 0)
print(answer)
